from datetime import datetime

from sqlmodel import Field

from ..enums import imperial, pantry
from ._base import TABLE_ID, Base, ForeignKey, Related, Table
from .inventory import ItemDimension


class ContainerDimension(Base, table=True):
    type: pantry.ContainerType
    size: float
    units: imperial.Volume


class ActionFact(Base, table=True):
    action: pantry.Action
    percent: float
    volume: imperial.Volume
    at: datetime


class LinkTable(Table, table=True):
    pantry_goodfact_uuid: TABLE_ID = Field(
        primary_key=True, foreign_key="pantry_goodfact.uuid"
    )
    pantry_actionfact_uuid: TABLE_ID = Field(
        primary_key=True, foreign_key="pantry_actionfact.uuid"
    )


class GoodFact(Base, table=True):
    inventory_itemdimension_uuid: TABLE_ID = ForeignKey(ItemDimension)
    item: ItemDimension = Related(ItemDimension)
    pantry_containerdimension_uuid: TABLE_ID = ForeignKey(ContainerDimension)
    container: ContainerDimension = Related(ContainerDimension)
    pantry_stocked_uuid: TABLE_ID = ForeignKey(ActionFact)
    stocked: ActionFact = Related(ActionFact, fieldname="pantry_stocked_uuid")
    pantry_opened_uuid: TABLE_ID | None = ForeignKey(ActionFact, default=None)
    opened: ActionFact = Related(ActionFact, fieldname="pantry_opened_uuid")
    consumed: list[ActionFact] = Related(ActionFact, link=LinkTable, auto=False)
    pantry_expired_uuid: TABLE_ID | None = ForeignKey(ActionFact, default=None)
    expired: ActionFact = Related(ActionFact, fieldname="pantry_expired_uuid")
    pantry_removed_uuid: ActionFact | None = ForeignKey(ActionFact, default=None)
    removed: ActionFact = Related(ActionFact, fieldname="pantry_removed_uuid")
    expiration_date: datetime | None = None
