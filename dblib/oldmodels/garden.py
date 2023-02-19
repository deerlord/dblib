from datetime import datetime, timedelta

from sqlmodel import Field, Relationship

from ..enums import garden
from ..models._base import TABLE_ID, Table
from ..models.inventory import ItemLink
from .location import GPSCoords


class RaisedBed(Table, table=True):
    gpscoords_id: TABLE_ID = Field(
        default=1, foreign_key=f"{GPSCoords.__tablename__}.id"
    )
    gpscoords: GPSCoords = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )


class Crop(ItemLink, table=True):
    raisedbed_id: TABLE_ID = Field(foreign_key=f"{RaisedBed.__tablename__}.id")
    raisedbed: RaisedBed = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    count: int = 0


class Action(Table, table=True):
    crop_id: TABLE_ID = Field(foreign_key=f"{Crop.__tablename__}.id")
    crop: Crop = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    count: int
    at: datetime
    stage: garden.Stage


class ScheduleData(Table, table=True):
    name: str
    germinated: timedelta
    planted: timedelta
    harvested: timedelta
