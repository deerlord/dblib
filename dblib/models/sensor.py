from sqlmodel import Field, Relationship

from ..enums import sensor as enums
from ._base import TABLE_ID, Base
from .location import GPSCoords


class Model(Base, table=True):
    number: enums.AdafruitModelNumber
    measurement: enums.Measurement


class Sensor(Base, table=True):
    sensor_model_uuid: TABLE_ID = Field(foreign_key=f"{Model.__tablename__}.uuid")
    model: Model = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Sensor.sensor_model_uuid",
        }
    )
    location_gpscoords_uuid: TABLE_ID | None = Field(
        foreign_key=f"{GPSCoords.__tablename__}.uuid"
    )
    coords: GPSCoords = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Sensor.location_gpscoords_uuid",
        }
    )
