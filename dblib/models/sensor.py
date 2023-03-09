from ..enums import sensor as enums
from ._base import Base


class Sensor(Base, table=True):
    model: enums.Model
    measurement: enums.Measurement
