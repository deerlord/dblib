from datetime import datetime
from typing import TypeAlias

from sqlalchemy.orm import declared_attr
from sqlmodel import Field, SQLModel

TABLE_ID: TypeAlias = int


class Table(SQLModel):
    id: TABLE_ID | None = Field(
        default=None, primary_key=True, index=True, nullable=False
    )
    updated_at: datetime | None = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}
    )
    created_at: datetime | None = Field(default_factory=datetime.utcnow)

    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        *_, module = cls.__module__.split(".")
        name = cls.__name__.lower()
        return f"{module.lower()}_{name}"
