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


class Stage(Table, table=True):
    count: int
    at: datetime


class Crop(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.id")
    item: Item = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    raisedbed_id: TABLE_ID = Field(foreign_key=f"{RaisedBed.__tablename__}.id")
    raisedbed: RaisedBed = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    count: int = 0

    germinated_id: TABLE_ID | None = Field(
        foreign_key=f"{Stage.__tablename__}.id"
    )
    germinated: Stage = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin", "foreign_keys": 'Crop.germinated_id'},
    )
    planted_id: TABLE_ID | None = Field(
        foreign_key=f"{Stage.__tablename__}.id"
    )
    planted: Stage = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin", "foreign_keys": 'Crop.planted_id'},
    )
    harvested_id: TABLE_ID | None = Field(
        foreign_key=f"{Stage.__tablename__}.id"
    )
    harvested: Stage = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin", "foreign_keys": 'Crop.harvested_id'},
    )


class ScheduleData(Table, table=True):
    name: str
    germinated: timedelta
    planted: timedelta
    harvested: timedelta
