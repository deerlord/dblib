from datetime import datetime

from sqlmodel import Field, Relationship

from ..models._base import TABLE_ID, Related, Table
from ..models.inventory import Item
from .sensors import Sensor


class Location(Table, Related(Item), table=True):
    time: datetime
    sensor_id: TABLE_ID = Field(foreign_key=f"{Sensor.__tablename__}.id")
    sensor: Sensor = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
