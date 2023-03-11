from enum import Enum, IntEnum


# adafruit product number
# https://www.adafruit.com/product/XXXX
class AdafruitModelNumber(IntEnum):
    soil_sensor = 4026


class Measurement(str, Enum):
    moisture = "moisture"
