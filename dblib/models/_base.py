from abc import ABC
from datetime import datetime
from typing import Generic, Type, TypeAlias, TypeVar

from pydantic import BaseModel, create_model
from pydantic.generics import GenericModel
from sqlalchemy.orm import declared_attr
from sqlmodel import Field, Relationship, SQLModel

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


def Related(model: Type[Table]) -> Type[BaseModel]:
    lowername = model.__name__.lower()
    modelname = f"{model.__name__.capitalize()}Relationship"
    tablename = model.__tablename__
    id_field = Field(foreign_key=f"{tablename}.id")
    id_name = f"{tablename}_id"
    related_field = Relationship(  # noqa: F821
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": f"{modelname}.{id_name}",
        },
    )
    fields = {
        id_name: (TABLE_ID, id_field),
        lowername: (model, related_field),
    }
    model = create_model(modelname, __base__=SQLModel, **fields)
    return model
