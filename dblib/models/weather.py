from ._base import Related, Table
from .location import GPSCoords
from datetime import datetime


class Alert(Table, Related(GPSCoords), table=True):
    noaa_id: str
    type: str
    sent: datetime
    effective: datetime
    onset: datetime
    expires: datetime
    ends: datetime
    status: str
    messageType: str
    category: str
    urgency: str
    event: str
    sender: str
    senderName: str
    headline: str
    description: str
    instruction: str
    response: str
