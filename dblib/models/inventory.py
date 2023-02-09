from datetime import datetime

from sqlmodel import Field, Relationship

from ..enums import inventory
from ._base import TABLE_ID, Table


class Item(Table, table=True):
    name: str
    type: inventory.ItemType


class Acquired(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.id")
    item: Item = Relationship()
    date: datetime
    location: str


class Liquidated(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.id")
    item: Item = Relationship()
    date: datetime
    location: str
