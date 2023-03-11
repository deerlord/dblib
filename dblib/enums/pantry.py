from enum import Enum


class Brand(str, Enum):
    heb = "heb"
    target = "target"
    imperial = "imperial"


class ContainerType(str, Enum):
    masonjar = "mason jar"
    box = "box"
