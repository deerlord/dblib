from datetime import datetime

from sqlmodel import Field, Relationship

from ..enums import imperial
from ._base import TABLE_ID, Table
from .inventory import ItemLink


class Container(Table, table=True):
    name: str
    units: imperial.Volume
    size: int


class StockedGood(ItemLink, table=True):
    container_id: TABLE_ID = Field(foreign_key=f"{Container.__tablename__}.id")
    container: Container = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    packed: datetime
    expires: datetime
    count: int
