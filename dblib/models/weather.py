from sqlmodel import UniqueConstraint
from ._base import Related, Table
from .location import GPSCoords
from datetime import datetime


class Alert(Table, Related(GPSCoords), table=True):
    __table_args__ = (UniqueConstraint("noaa_id"),)
    noaa_id: str
    type: str
    sent: datetime
    effective: datetime
    onset: datetime
    expires: datetime
    ends: datetime
    status: str
    message_type: str
    category: str
    urgency: str
    event: str
    sender: str
    sender_name: str
    headline: str
    description: str
    instruction: str | None = None
    response: str