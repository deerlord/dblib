from enum import Enum


class Action(str, Enum):
    stocked = "stocked"
    opened = "opened"
    expired = "expired"
    consumed = "consumed"
    thrownout = "thrown out"


class ContainerType(str, Enum):
    masonjar = "mason jar"
    box = "box"
