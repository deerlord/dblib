from datetime import datetime

from sqlmodel import Field

from ..types import TABLE_ID
from ._base import Table
from .inventory import Item  # noqa: F401


class Planted(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.id")
    datetime: datetime
    location: str
    count: str


class Harvested(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.id")
    datetime: datetime
    location: str
    count: str
