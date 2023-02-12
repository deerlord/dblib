from datetime import datetime, timedelta

from sqlmodel import Field, Relationship

from ._base import TABLE_ID, Table
from .inventory import Item
from .location import GPSCoords


class RaisedBed(Table, table=True):
    gpscoords_id: TABLE_ID = Field(
        default=1, foreign_key=f"{GPSCoords.__tablename__}.id"
    )
    gpscoords: GPSCoords = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )


class Plant(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.id")
    item: Item = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    raisedbed_id: TABLE_ID = Field(foreign_key=f"{RaisedBed.__tablename__}.id")
    raisedbed: RaisedBed = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    germinated: datetime | None = None
    planted: datetime | None = None
    harvested: datetime | None = None


class ScheduleData(Table, table=True):
    name: str
    germinated: timedelta
    planted: timedelta
    harvested: timedelta
