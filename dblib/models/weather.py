from datetime import datetime
from ._base import Table


class Forecast(Table, table=True):
    startTime: datetime
    endTime: datetime
    isDaytime: bool
    temperature: int
    temperatureUnit: str
    probabilityOfPrecipitation: float
    dewpoint: float
    relativeHumidity: float
    windspeed: str
    windDirection: str
    icon: str
    shortForecast: str
    detailedForecast: str
