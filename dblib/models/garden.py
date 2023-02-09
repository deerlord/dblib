from datetime import datetime, timedelta

from sqlmodel import Field

from ._base import TABLE_ID, Table
from .inventory import Item
from .location import GPSCoords


class RaisedBed(Table, table=True):
    coords_id: TABLE_ID = Field(foreign_key=f"{GPSCoords.__tablename__}.id")


class Plant(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.id")
    raisedbed_id: TABLE_ID | None = Field(default=None, foreign_key=f"{RaisedBed.__tablename__}.id")
    germinated: datetime | None = None
    planted: datetime | None = None
    harvested: datetime | None = None


class ScheduleData(Table, table=True):
    name: str
    germinated: timedelta
    planted: timedelta
    harvested: timedelta
