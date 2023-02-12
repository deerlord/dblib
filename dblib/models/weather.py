from datetime import datetime
from ._base import Table


class Forecast(Table, table=True):
    latitude: float
    longitude: float
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
