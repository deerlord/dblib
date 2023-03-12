from datetime import datetime

from sqlmodel import Field, Relationship, UniqueConstraint

from ._base import TABLE_ID, Base
from .location import GPSCoords


class Alert(Base, table=True):
    __table_args__ = (UniqueConstraint("noaa_id"),)
    location_gpscoords_uuid: TABLE_ID = Field(
        foreign_key=f"{GPSCoords.__tablename__}.uuid"
    )
    gpscoords: GPSCoords = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Alert.location_gpscoords_uuid",
        }
    )
    noaa_id: str
    sent: datetime
    effective: datetime
    onset: datetime | None = None
    expires: datetime
    ends: datetime | None = None
    status: str
    message_type: str
    category: str
    urgency: str
    event: str
    sender: str
    sender_name: str
    headline: str | None = None
    description: str
    instruction: str | None = None
    response: str
