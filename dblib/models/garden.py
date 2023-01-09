from datetime import datetime

from sqlmodel import Field

from ._base import TABLE_ID, Table
from .inventory import Item


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
