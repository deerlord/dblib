from ._base import Table


class Sensor(Table, table=True):
    name: str
    latitude: float
    longitude: float
    elevation: float
