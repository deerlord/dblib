from pydantic.main import BaseModel
from sqlmodel import Field, SQLModel

from ..types import TABLE_ID


class Table(SQLModel):
    id: TABLE_ID | None = Field(default=None, primary_key=True)


class SearchModel(BaseModel):
    class Config:
        validate_assignment = True
