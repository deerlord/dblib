from ._base import Table
import uuid


class Sensor(Table, table=True):
    uuid: uuid.UUID
    name: str
    latitude: float
    longitude: float
    elevation: float
