from enum import Enum


class Action(str, Enum):
    stocked = "stocked"
    opened = "opened"
    expired = "expired"
    consumed = "consumed"
    removed = "removed"


class Brand(str, Enum):
    heb = "heb"
    target = "target"
    imperial = "imperial"


class ContainerType(str, Enum):
    masonjar = "mason jar"
    box = "box"
