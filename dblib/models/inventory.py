from datetime import datetime

from sqlmodel import Field, Relationship

from ..enums import inventory
from ._base import TABLE_ID, Table


class Item(Table, table=True):
    name: str
    type: inventory.ItemType = Field(index=True)


class ItemLink(Table):
    item_id: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.id")
    item: Item = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
