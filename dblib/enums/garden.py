from enum import Enum


class Stage(str, Enum):
    germinat = "germinated"
    plant = "planted"
    harvest = "harvested"


class IrrigationHoseType(str, Enum):
    driptape = "driptape"
    driptube = "driptube"
