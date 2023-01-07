from datetime import datetime
from typing import TypeAlias

from pydantic import BaseModel
from sqlmodel import Field, SQLModel

TABLE_ID: TypeAlias = int | None


class GPS(BaseModel):
    latitude: float
    longitude: float


class UpdateLocation(BaseModel):
    dev_name: str
    sensor_name: str


class Table(SQLModel):
    id: TABLE_ID = Field(default=None, primary_key=True)


class Sensor(Table, table=True):
    name: str
    latitude: float
    longitude: float


class Device(Table, table=True):
    name: str


class Location(Table, table=True):
    time: datetime
    dev_name: str | None = Field(default=None, foreign_key="device.name")
    sensor_name: str | None = Field(default=None, foreign_key="sensor.name")
