from datetime import datetime

from sqlmodel import Field, SQLModel

from ..enums import general
from ..types import TABLE_ID
from ._base import Table
from .general import Item  # noqa: F401


class ToDo(Table, table=True):
    name: str
    description: str
    due_by: datetime | None = None
    completed: datetime | None = None
    category: general.Category = Field(default=general.Category.general)
    item_id: TABLE_ID | None = Field(default=None, foreign_key="item.id")


class Block(SQLModel, table=True):
    blocker_id: TABLE_ID = Field(primary_key=True, foreign_key="todo.id")
    blocked_id: TABLE_ID = Field(primary_key=True, foreign_key="todo.id")
