from datetime import datetime

from sqlmodel import Field, Relationship, SQLModel

from ..enums import tasks
from ..models._base import TABLE_ID, Table


class Action(Table, table=True):
    name: str
    description: str
    due_by: datetime | None = None
    completed: datetime | None = None
    category: tasks.Category = Field(default=tasks.Category.general)


class Block(SQLModel, table=True):
    blocker_id: TABLE_ID = Field(
        primary_key=True, foreign_key=f"{Action.__tablename__}.id"
    )
    blocker: Action = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin", "foreign_keys": "Block.blocker_id"},
    )
    blocked_id: TABLE_ID = Field(
        primary_key=True, foreign_key=f"{Action.__tablename__}.id"
    )
    blocked: Action = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin", "foreign_keys": "Block.blocked_id"},
    )
