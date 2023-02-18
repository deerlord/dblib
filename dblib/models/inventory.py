from datetime import datetime

from sqlmodel import Field, Relationship

from ..enums import inventory
from ._base import TABLE_ID, Table


class Data(Table, table=True):
    name: str
    type: inventory.ItemType = Field(index=True)



class Item(Table, table=True):
    data_id: TABLE_ID = Field(foreign_key=f"{Data.__tablename__}.id")
    data: Data = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    expires: datetime | None = None


class Change(Table, table=True):
    item_id: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.id")
    item: Item = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )
    date: datetime
    location: str
    action: inventory.Action
