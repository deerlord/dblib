from datetime import datetime

from sqlmodel import Field, Relationship

from ..enums import imperial
from ._base import TABLE_ID, Table
from .inventory import Item


class Container(Table, table=True):
    name: str
    units: imperial.Volume
    size: int


class StockedGood(Table, table=True):
    ingredient_id: TABLE_ID = Field(
        default=None, foreign_key=f"{Item.__tablename__}.id"
    )

    ingredient: Item = Relationship()
    container_id: TABLE_ID = Field(
        default=None, foreign_key=f"{Container.__tablename__}.id"
    )
    packed: datetime
    expires: datetime
    count: int


class OpenedGood(Table, table=True):
    stockedgood_id: TABLE_ID = Field(
        default=None, foreign_key=f"{StockedGood.__tablename__}.id"
    )
    opened: datetime
    percent: float = 100.0
    emptied: datetime | None = None
