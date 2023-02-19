from datetime import datetime

from sqlmodel import Field, Relationship

from ..models.inventory import ItemLink
from ._base import TABLE_ID, Table
from .sensors import Sensor


class Location(ItemLink, table=True):
    time: datetime
    sensor_id: TABLE_ID = Field(foreign_key=f"{Sensor.__tablename__}.id")
    sensor: Sensor = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
