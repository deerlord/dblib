from datetime import datetime

from sqlmodel import Field

from ..enums import tasks
from ..models._base import Related, Table


class Action(Table, table=True):
    name: str
    description: str
    due_by: datetime | None = None
    completed: datetime | None = None
    category: tasks.Category = Field(default=tasks.Category.general)


class Block(Table, Related(Action, "blocker"), Related(Action, "blocked"), table=True):
    active: bool = True
