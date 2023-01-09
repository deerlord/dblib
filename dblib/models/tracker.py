from datetime import datetime

from sqlmodel import Field

from ._base import TABLE_ID, Table
from .bluetooth import Device
from .sensors import Sensor


class Location(Table, table=True):
    time: datetime
    device_id: TABLE_ID = Field(default=None, foreign_key=f"{Device.__tablename__}.id")
    sensor_id: TABLE_ID = Field(default=None, foreign_key=f"{Sensor.__tablename__}.id")
