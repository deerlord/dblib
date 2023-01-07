from enum import Enum


class Volume(str, Enum):
    teaspoon = "tsp"
    tablespoon = "tbsp"
    ounce = "ounce"
    cup = "cup"
    pint = "pint"
    quart = "quart"
    gallon = "gallon"
