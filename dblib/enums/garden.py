from enum import Enum


class Stage(str, Enum):
    germinated = "germinated"
    planted = "planted"
    harvested = "harvested"
