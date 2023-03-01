from datetime import datetime
from typing import Type, TypeAlias, TypeVar
from uuid import UUID

from pydantic import create_model
from sqlalchemy.orm import declared_attr
from sqlmodel import Field, Relationship, SQLModel

TABLE_ID: TypeAlias = UUID
T = TypeVar("T", bound="Table")


class Table(SQLModel):
    uuid: TABLE_ID | None = Field(
        default_factory=None, index=True, primary_key=True, nullable=False
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


def Related(
    model: Type[Table], fieldname: str | None = None, nullable: bool = False
) -> Type[SQLModel]:
    tablename = model.__tablename__
    kwargs = {}
    if nullable:
        id_type = TABLE_ID | None
        kwargs.update({"default": None})
    else:
        id_type = TABLE_ID
    id_field = Field(foreign_key=f"{tablename}.uuid", nullable=nullable, **kwargs)
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
        id_name: (id_type, id_field),
        lowername: (model, related_field),
    }
    model = create_model(modelname, __base__=SQLModel, **fields)
    return model
