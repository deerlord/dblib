from datetime import datetime

from ..models._base import Base


class Message(Base, table=True):
    topic: str
    timestamp: datetime
    payload: bytes
    acked: bool = False
