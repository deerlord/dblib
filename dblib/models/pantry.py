from datetime import datetime

from sqlmodel import Field

from .. import types
from ..enums import imperial
from ._base import Table
from .inventory import Item


class Container(Table, table=True):
    name: str
    units: imperial.Volume
    size: int


class StockedGood(Table, table=True):
    ingredient_id: types.TABLE_ID = Field(
        default=None, foreign_key=f"{Item.__tablename__}.id"
    )
    container_id: types.TABLE_ID = Field(
        default=None, foreign_key=f"{Container.__tablename__}.id"
    )
    packed: datetime
    expires: datetime
    count: int


class OpenedGood(Table, table=True):
    stockedgood_id: types.TABLE_ID = Field(
        default=None, foreign_key=f"{StockedGood.__tablename__}.id"
    )
    opened: datetime
    percent: float = 100.0
