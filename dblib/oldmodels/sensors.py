from datetime import datetime
from uuid import UUID

from sqlmodel import Field, Relationship

from ..models.inventory import Item
from ..models.location import GPSCoords
from ..models._base import Table, TABLE_ID, Related



class Sensor(Table, Related(Item), table=True):
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
