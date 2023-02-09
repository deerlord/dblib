from ._base import Table


class GPSCoords(Table, table=True):
    latitude: float
    longitude: float
    elevation: float | None = None
