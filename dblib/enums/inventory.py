from enum import Enum


class ItemType(str, Enum):
    sensor = "sensor"
    ingredient = "ingredient"
    plant = "plant"
    equipment = "equipment"
    device = "device"
