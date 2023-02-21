from datetime import datetime, timedelta

from ..enums import garden
from ._base import Related, Table
from .inventory import Item
from .location import GPSCoords


class RaisedBed(Table, Related(GPSCoords), table=True):
    width: float
    length: float
    height: float


class Crop(Table, Related(Item), Related(RaisedBed), table=True):
    count: int = 0


class Action(Table, Related(Crop), table=True):
    count: int
    at: datetime
    stage: garden.Stage


class ScheduleData(Table, Related(Item), table=True):
    germinated: timedelta
    planted: timedelta
    harvested: timedelta
