from datetime import datetime

from sqlalchemy import UniqueConstraint
from sqlmodel import Field, Relationship

from ._base import TABLE_ID, Table
from .location import GPSCoords


class QuantitativeValue(Table, table=True):
    value: float
    max_value: float
    min_value: float
    unit_code: str
    quality_control: str


class Forecast(Table, table=True):
    __table_args__ = (UniqueConstraint("gpscoords_id", "start_time", "end_time"),)
    gpscoords_id: TABLE_ID = Field(foreign_key=f"{GPSCoords.__tablename__}.id")
    gpscoords: GPSCoords = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    start_time: datetime
    end_time: datetime
    is_daytime: bool
    temperature_trend: str
    probability_of_precipitation_id: TABLE_ID = Field(
        foreign_key=f"{QuantitativeValue.__tablename__}.id"
    )
    probability_of_precipitation: QuantitativeValue = Relationship(  # noqa: F821
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Forecast.probability_of_precipitation_id",
        },
    )
    dewpoint_id: TABLE_ID = Field(foreign_key=f"{QuantitativeValue.__tablename__}.id")
    dewpoint: QuantitativeValue = Relationship(  # noqa: F821
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Forecast.dewpoint_id",
        },
    )
    relative_humidity_id: TABLE_ID = Field(
        foreign_key=f"{QuantitativeValue.__tablename__}.id"
    )
    relative_humidity: QuantitativeValue = Relationship(  # noqa: F821
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Forecast.relative_humidity_id",
        },
    )
    wind_direction: str
    short_forecast: str
    detailed_forecast: str
