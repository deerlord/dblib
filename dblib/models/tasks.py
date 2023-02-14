from datetime import datetime

from sqlmodel import Field, Relationship

from ..enums import tasks
from ._base import TABLE_ID, Table
from .inventory import Item


class Action(Table, table=True):
    name: str
    description: str
    due_by: datetime | None = None
    completed: datetime | None = None
    category: tasks.Category = Field(default=tasks.Category.general)
    item_id: TABLE_ID | None = Field(
        default=None, foreign_key=f"{Item.__tablename__}.id"
    )
    item: Item = Relationship(  # noqa: F821
        sa_relationship_kwargs={"lazy": "selectin"},
    )


# class Block(Table, table=True):
#     blocker_id: TABLE_ID = Field(
#         primary_key=True, foreign_key=f"{Action.__tablename__}.id"
#     )
#     blocker: Action = Relationship(  # noqa: F821
#         sa_relationship_kwargs={"lazy": "selectin"},
#     )
#     blocked_id: TABLE_ID = Field(
#         primary_key=True, foreign_key=f"{Action.__tablename__}.id"
#     )
#     blocked: Action = Relationship(  # noqa: F821
#         sa_relationship_kwargs={"lazy": "selectin"},
#     )
