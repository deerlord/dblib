from datetime import datetime

from ..enums import imperial, pantry
from ._base import Related, Table
from .inventory import Item


class Container(Table, table=True):
    name: str
    units: imperial.Volume
    size: float


class StockedGood(Table, Related(Item), table=True):
    container: Container
    packed: datetime
    expires: datetime
    count: int


class Consumed(Table, Related(StockedGood), table=True):
    at: datetime
    amount: float
    unit: pantry.UnitContainer
