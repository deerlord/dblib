from datetime import datetime
from typing import Generator

from sqlmodel import Relationship

from ..enums import imperial, pantry
from ._base import TABLE_ID, Base, ForeignKey
from .inventory import ItemDimension


class ContainerDimension(Base, table=True):
    type: pantry.ContainerType
    size: float
    units: imperial.Volume


class GoodFact(Base, table=True):
    inventory_itemdimension_uuid: TABLE_ID = ForeignKey(ItemDimension)
    item: ItemDimension = Relationship()
    pantry_containerdimension_uuid: TABLE_ID = ForeignKey(ContainerDimension)
    container: ContainerDimension = Relationship()
    actions: list["ActionFact"] = Relationship(
        back_populates="good", sa_relationship_kwargs={"lazy": "selectin"}
    )
    expiration_date: datetime | None = None

    @property
    def stocked(self) -> "ActionFact":
        return self._single_action(pantry.Action.stocked)

    @property
    def opened(self) -> "ActionFact":
        return self._single_action(pantry.Action.opened)

    @property
    def consumed(self) -> Generator["ActionFact", None, None]:
        for action in self.actions:
            if action.action == pantry.Action.consumed:
                yield action

    @property
    def expired(self) -> "ActionFact":
        return self._single_action(pantry.Action.expired)
    
    @property
    def thrown_out(self) -> "ActionFact":
        return self._single_action(pantry.Action.thrownout)

    def remaining(self, units: imperial.Volume) -> float:
        stocked = self._unit_converter(self.stocked.amount, self.stocked.units, units)
        expired = self._unit_converter(self.expired.amount, self.expired.units, units)
        consumed = sum(
            self._unit_converter(fact.amount, fact.units, units)
            for fact in self.consumed
        )
        total = stocked - expired - consumed
        return total

    def _unit_converter(
        self, amount: float, input_units: imperial.Volume, output_units: imperial.Volume
    ) -> float:
        return amount * UnitFactors[input_units] / UnitFactors[output_units]

    def _single_action(self, action: pantry.Action) -> "ActionFact":
        for a in self.actions:
            if a.action == action:
                return a
        message = f"No {action.value} action found on {self.__class__.__name__} with UUID {self.uuid}"
        raise AttributeError(message)


class ActionFact(Base, table=True):
    pantry_goodfact_uuid: TABLE_ID = ForeignKey(GoodFact)
    good: GoodFact = Relationship(back_populates="actions")
    action: pantry.Action
    amount: float
    units: imperial.Volume
    at: datetime


UnitFactors = {
    imperial.Volume.teaspoon: 1.0,
    imperial.Volume.tablespoon: 3.0,
    imperial.Volume.ounce: 6.0,
    imperial.Volume.cup: 48.0,
    imperial.Volume.pint: 96.0,
    imperial.Volume.quart: 192.0,
    imperial.Volume.gallon: 768.0,
}
