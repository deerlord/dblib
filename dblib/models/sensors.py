from datetime import datetime
from uuid import UUID

from sqlmodel import Field, Relationship

from ._base import TABLE_ID, Table
from .inventory import Item
from .location import GPSCoords


class Sensor(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.id")
    item: Item = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    gpscoords_id: TABLE_ID = Field(
        default=1, foreign_key=f"{GPSCoords.__tablename__}.id"
    )
    gpscoords: GPSCoords = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )


class Data(Table, table=True):
    timestamp: datetime
    uuid: UUID = Field(index=True)
    measurement: str = Field(index=True)
    value: float
