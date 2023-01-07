from datetime import datetime

from sqlmodel import Field

from ..types import TABLE_ID
from ._base import Table


class Item(Table, table=True):
    name: str


class Acquired(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key="item.id")
    date: datetime
    location: str


class Liquidated(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key="item.id")
    date: datetime
    location: str
