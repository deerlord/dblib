from sqlmodel import Field, SQLModel

from ..types import TABLE_ID


class Table(SQLModel):
    id: TABLE_ID | None = Field(default=None, primary_key=True)

    @property
    def __tablename__(self) -> str:
        *_, module = self.__module__.split(".")
        name = self.__class__.__name__.lower()
        return f"{module}_{name}"
