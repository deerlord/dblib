from sqlalchemy import UniqueConstraint

from ..models._base import Table


class GPSCoords(Table, table=True):
    __table_args__ = (UniqueConstraint("latitude", "longitude", "elevation"),)
    latitude: float
    longitude: float
    elevation: float | None = None
