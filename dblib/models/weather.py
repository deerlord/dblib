from datetime import datetime

from sqlmodel import UniqueConstraint

from ._base import Table, Related
from .location import GPSCoords


class Alert(Table, Related(GPSCoords), table=True):
    __table_args__ = (UniqueConstraint("noaa_id"),)
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
