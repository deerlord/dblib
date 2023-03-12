from enum import Enum


class Action(str, Enum):
    stocked = "stocked"
    consumed = "consumed"
    dispoed = "disposed"
