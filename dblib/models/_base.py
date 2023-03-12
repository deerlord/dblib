from datetime import datetime
from typing import Type, TypeAlias, TypeVar
from uuid import UUID, uuid4

from sqlalchemy.orm import declared_attr
from sqlmodel import Field, Relationship, SQLModel

TABLE_ID: TypeAlias = UUID
T = TypeVar("T", bound="Table")


class Table(SQLModel):
    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        *_, module = cls.__module__.split(".")
        name = cls.__name__.lower()
        return f"{module.lower()}_{name}"


class Base(Table):
    uuid: TABLE_ID = Field(
        default_factory=uuid4, index=True, primary_key=True, nullable=False
    )
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}
    )

    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        *_, module = cls.__module__.split(".")
        name = cls.__name__.lower()
        return f"{module.lower()}_{name}"


def ForeignKey(model: Type[Table], **kwargs):
    field = Field(foreign_key=f"{model.__tablename__}.uuid", index=True, **kwargs)
    return field
