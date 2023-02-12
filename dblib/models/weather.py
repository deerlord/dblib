from datetime import datetime
from ._base import Table, TABLE_ID
from sqlmodel import Field
from .location import GPSCoords


class Forecast(Table, table=True):
    gpscoords_id: TABLE_ID = Field(default=1, foreign_key=f"{GPSCoords.__tablename__}.id")
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
