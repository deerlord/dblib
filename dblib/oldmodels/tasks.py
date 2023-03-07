from datetime import datetime

from sqlmodel import Field

from ..enums import tasks
from ..models._base import Base, Related


class Action(Base, table=True):
    name: str
    description: str
    due_by: datetime | None = None
    completed: datetime | None = None
    category: tasks.Category = Field(default=tasks.Category.general)


class Block(Base, Related(Action, "blocker"), Related(Action, "blocked"), table=True):
    active: bool = True
