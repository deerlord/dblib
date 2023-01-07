from datetime import datetime

from sqlmodel import Field

from .. import types
from ..enums import imperial
from ._base import Table
from .general import Item  # noqa: F401


class Container(Table, table=True):
    name: str
    units: imperial.Volume
    size: int


class StockedGood(Table, table=True):
    ingredient_id: types.TABLE_ID = Field(default=None, foreign_key="item.id")
    container_id: types.TABLE_ID = Field(default=None, foreign_key="container.id")
    packed: datetime
    expires: datetime
    count: int


class OpenedGood(Table, table=True):
    stockedgood_id: types.TABLE_ID = Field(default=None, foreign_key="stockedgood.id")
    opened: datetime
    percent: float = 100.0
