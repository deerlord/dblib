from datetime import datetime
from typing import Type, TypeAlias
from uuid import UUID, uuid4

from pydantic import BaseModel, create_model
from sqlalchemy.orm import declared_attr
from sqlmodel import Field, Relationship, SQLModel, UniqueConstraint

TABLE_ID: TypeAlias = int


class Table(SQLModel):
    __table_args__ = (UniqueConstraint("uuid"),)
    id: TABLE_ID | None = Field(
        default=None, primary_key=True, index=True, nullable=False
    )
    uuid: UUID = Field(default_factory=uuid4, index=True)
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(
        default_factory=datetime.utcnow, sa_column_kwargs={"onupdate": datetime.utcnow}
    )

    @declared_attr  # type: ignore
    def __tablename__(cls) -> str:
        *_, module = cls.__module__.split(".")
        name = cls.__name__.lower()
        return f"{module.lower()}_{name}"


def Related(model: Type[Table], fieldname: str | None = None) -> Type[BaseModel]:
    tablename = model.__tablename__
    id_field = Field(foreign_key=f"{tablename}.uuid")
    if fieldname:
        lowername = fieldname.lower()
        id_name = f"{lowername}_uuid"
        modelname = f"{model.__name__}As{fieldname.capitalize()}Relationship"
    else:
        lowername = model.__name__.lower()
        id_name = f"{tablename.lower()}_uuid"
        modelname = f"{model.__name__}Relationship"
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
