from enum import Enum, IntEnum


class Model(IntEnum):
    soil_sensor = 4026


class Measurement(str, Enum):
    moisture = "moisture"
