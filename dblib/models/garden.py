from datetime import datetime
from ._base import Table
from ..types import TABLE_ID
from sqlmodel import Field
from .inventory import Item  # noqa: F401


class Planted(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key="item.id")
    date: datetime
    location: str
    count: str


class Harvested(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key="item.id")
    date: datetime
    location: str
    count: str
