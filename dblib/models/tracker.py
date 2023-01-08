from datetime import datetime

from sqlmodel import Field

from ..types import TABLE_ID
from ._base import Table
from .bluetooth import Device


class Sensor(Table, table=True):
    name: str
    latitude: float
    longitude: float


class Location(Table, table=True):
    time: datetime
    device_id: TABLE_ID = Field(default=None, foreign_key=f"{Device.__tablename__}.id")
    sensor_id: TABLE_ID = Field(default=None, foreign_key=f"{Sensor.__tablename__}.id")
