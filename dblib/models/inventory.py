from sqlmodel import Field

from ..enums import inventory
from ._base import Base


class Item(Base, table=True):
    name: str
    type: inventory.ItemType = Field(index=True)
