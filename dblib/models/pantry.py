from datetime import datetime

from ..enums import imperial, pantry
from ._base import TABLE_ID, Base, ForeignKey, Related
from .inventory import ItemDimension


class ContainerDimension(Base, table=True):
    type: pantry.ContainerType
    size: float
    units: imperial.Volume


class GoodFact(Base, table=True):
    inventory_itemdimension_uuid: TABLE_ID = ForeignKey(ItemDimension)
    item: ItemDimension = Related(ItemDimension)
    pantry_containerdimension_uuid: TABLE_ID = ForeignKey(ContainerDimension)
    container: ContainerDimension = Related(ContainerDimension)


class ActionFact(Base, table=True):
    pantry_goodfact_uuid: TABLE_ID = ForeignKey(GoodFact)
    action: pantry.Action
    amount: float
    units: imperial.Volume
    at: datetime
