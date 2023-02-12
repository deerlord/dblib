from datetime import datetime

from sqlmodel import Field, Relationship

from ._base import TABLE_ID, Table
from .inventory import Item
from .sensors import Sensor


class Location(Table, table=True):
    time: datetime
    item_id: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.id")
    item: Item = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    sensor_id: TABLE_ID = Field(foreign_key=f"{Sensor.__tablename__}.id")
    sensor: Sensor = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
