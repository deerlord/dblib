from sqlmodel import Field, Relationship, UniqueConstraint

from ._base import TABLE_ID, Base, Table


class LinkTable(Table, table=True):
    location_polygon_uuid: TABLE_ID | None = Field(
        default=None, primary_key=True, foreign_key="location_polygon.uuid"
    )
    location_gpscoords_uuid: TABLE_ID | None = Field(
        default=None, primary_key=True, foreign_key="location_gpscoords.uuid"
    )


class Polygon(Base, table=True):
    coords: list["GPSCoords"] = Relationship(
        link_model=LinkTable,
        sa_relationship_kwargs={"lazy": "selectin"},
    )


class GPSCoords(Base, table=True):
    __table_args__ = (UniqueConstraint("latitude", "longitude", "elevation"),)
    latitude: float
    longitude: float
    elevation: float | None = None
