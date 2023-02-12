from datetime import datetime

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship

from ._base import TABLE_ID, Table
from .location import GPSCoords


class Forecast(Table, table=True):
    __table_args__ = (UniqueConstraint("gpscoords_id", "start_time", "end_time"),)
    gpscoords_id: TABLE_ID = Field(
        default=1, foreign_key=f"{GPSCoords.__tablename__}.id"
    )
    gpscoords: GPSCoords = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    start_time: datetime
    end_time: datetime
    is_daytime: bool
    temperature: int
    temperature_unit: str
    probability_of_precipitation: float | None = None
    dewpoint: float | None = None
    relative_humidity: float | None = None
    windspeed: str
    wind_direction: str
    icon: str
    short_forecast: str
    detailed_forecast: str
