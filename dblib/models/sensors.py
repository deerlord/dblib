from sqlmodel import Field

from ._base import TABLE_ID, Table
from .inventory import Item
from .location import GPSCoords


class Sensor(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.id")
    coords_id: TABLE_ID = Field(foreign_key=f"{GPSCoords.__tablename__}.id")
