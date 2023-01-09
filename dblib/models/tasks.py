from datetime import datetime

from sqlmodel import Field, SQLModel

from ..enums import tasks
from ._base import TABLE_ID, Table
from .inventory import Item


class ToDo(Table, table=True):
    name: str
    description: str
    due_by: datetime | None = None
    completed: datetime | None = None
    category: tasks.Category = Field(default=tasks.Category.general)
    item_id: TABLE_ID | None = Field(
        default=None, foreign_key=f"{Item.__tablename__}.id"
    )


class Block(SQLModel, table=True):
    blocker_id: TABLE_ID = Field(
        primary_key=True, foreign_key=f"{ToDo.__tablename__}.id"
    )
    blocked_id: TABLE_ID = Field(
        primary_key=True, foreign_key=f"{ToDo.__tablename__}.id"
    )
