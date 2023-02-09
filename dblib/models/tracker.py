from datetime import datetime

from sqlmodel import Field

from ._base import TABLE_ID, Table
from .inventory import Item
from .sensors import Sensor


class Location(Table, table=True):
    time: datetime
    item_id: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.id")
    sensor_id: TABLE_ID = Field(foreign_key=f"{Sensor.__tablename__}.id")
