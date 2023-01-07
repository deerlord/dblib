from datetime import datetime

from sqlmodel import Field, SQLModel

from ..types import TABLE_ID
from ._base import Table


class ToDo(Table, table=True):
    name: str
    description: str
    due_by: datetime | None = None
    completed: datetime | None = None


class Block(SQLModel, table=True):
    blocker_id: TABLE_ID = Field(primary_key=True, foreign_key="todo.id")
    blocked_id: TABLE_ID = Field(primary_key=True, foreign_key="todo.id")
