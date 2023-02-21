from sqlmodel import Field

from ..enums import inventory
from ._base import Table


class Item(Table, table=True):
    name: str
    type: inventory.ItemType = Field(index=True)
