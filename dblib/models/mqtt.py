from datetime import datetime
from ._base import Table


class Message(Table, table=True):
    topic: str
    timestamp: datetime
    payload: bytes
    acked: bool = False
