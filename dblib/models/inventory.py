from datetime import datetime

from sqlmodel import Field

from ._base import TABLE_ID, Table


class Item(Table, table=True):
    name: str


class Acquired(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.id")
    date: datetime
    location: str


class Liquidated(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.id")
    date: datetime
    location: str
