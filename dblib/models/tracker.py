from datetime import datetime

from sqlmodel import Field

from ..types import TABLE_ID
from ._base import Table


class Sensor(Table, table=True):
    name: str
    latitude: float
    longitude: float


class Device(Table, table=True):
    name: str


class Location(Table, table=True):
    time: datetime
    device_id: TABLE_ID = Field(default=None, foreign_key="device.id")
    sensor_id: TABLE_ID = Field(default=None, foreign_key="sensor.id")
