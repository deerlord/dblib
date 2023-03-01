from datetime import datetime, timedelta

from sqlmodel import UniqueConstraint

from ..enums import garden
from ._base import Related, Table
from .inventory import Item
from .location import GPSCoords


class IrrigationHose(Table, table=True):
    __table_args__ = (
        UniqueConstraint("type", "emitters_per_foot", "gallons_per_hour"),
    )
    name: str
    type: garden.IrrigationHoseType
    emitters_per_foot: float
    gallons_per_hour: float


class IrrigationGrid(Table, Related(IrrigationHose), table=True):
    length: float
    row_count: int


class RaisedBed(
    Table, Related(GPSCoords), Related(IrrigationGrid, nullable=True), table=True
):
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
