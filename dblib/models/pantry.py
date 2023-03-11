from datetime import datetime

from sqlmodel import Field, Relationship

from ..enums import imperial, pantry
from ._base import TABLE_ID, Base, Table
from .inventory import Item


class Container(Base, table=True):
    type: pantry.ContainerType
    units: imperial.Volume
    size: float


class Good(Base, table=True):
    brand: str
    inventory_item_uuid: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.uuid")
    item: Item = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Good.inventory_item_uuid",
        }
    )
    pantry_container_uuid: TABLE_ID = Field(
        foreign_key=f"{Container.__tablename__}.uuid"
    )
    container: Container = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Good.pantry_container_uuid",
        }
    )


class Stocked(Base, table=True):
    pantry_good_uuid: TABLE_ID = Field(foreign_key=f"{Good.__tablename__}.uuid")
    good: Good = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Stocked.pantry_good_uuid",
        }
    )
    at: datetime
    amount: float
    expires: datetime


class Consumed(Base, table=True):
    pantry_good_uuid: TABLE_ID = Field(foreign_key=f"{Good.__tablename__}.uuid")
    good: Good = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Consumed.pantry_good_uuid",
        }
    )
    at: datetime
    amount: datetime
