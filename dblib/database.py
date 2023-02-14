import importlib
import os
import pkgutil
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Generator, Type, TypeAlias, TypeVar

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel, select
from sqlmodel.sql.expression import SelectOfScalar

from . import models
from .settings import Settings
from sqlalchemy.exc import IntegrityError

T = TypeVar("T")
S = TypeVar("S", bound=SQLModel)

settings = Settings()



SESSION: TypeAlias = AsyncSession


def connection_string():
    settings = Settings()
    strings = {
        "postgres": (
            "postgresql+asyncpg://{database_username}:{database_password}"
            "@{database_hostname}:{database_port}/{database_name}"
        ),
        "sqlite": "sqlite+aiosqlite://{database_name}",
    }
    string = strings[settings.database_protocol]
    return string.format(**settings.dict())


def engine() -> AsyncEngine:
    string = connection_string()
    return create_async_engine(string)


session = sessionmaker(engine(), expire_on_commit=False, class_=SESSION)


@asynccontextmanager
async def connection() -> AsyncGenerator[SESSION, None]:
    async with session() as local:
        try:
            yield local
            await local.commit()
        except IntegrityError:
            await local.rollback()


async def get_all(statement: SelectOfScalar[S]) -> AsyncGenerator[S, None]:  # type: ignore
    async with connection() as db:
        results = await db.execute(statement)
        for result in results.fetchall():
            yield result  # type: ignore


async def get_relationship(parent: SQLModel, foreign: Type[S]) -> S | None:
    key = f"{foreign.__name__.lower()}_id"
    retval = None
    fk_id = getattr(parent, key, None)
    if fk_id is None:
        return retval
    statement = select(foreign).where(foreign.id == fk_id)
    async for result in get_all(statement):
        retval = result
        break
    return retval


def data_models(name: str | None = None) -> dict[str, list[Type[SQLModel]]]:
    pkgpath = os.path.dirname(models.__file__)
    packages = (
        package
        for _, package, _ in pkgutil.iter_modules([pkgpath])
        if not package.startswith("_")
        if not name or package == name
    )
    retval = {package: list(_get_models(package)) for package in packages}
    return retval


def _get_models(package: str) -> Generator[Type[SQLModel], None, None]:
    module = importlib.import_module(f"dblib.models.{package}")
    classes = (
        getattr(module, model) for model in dir(module) if not model.startswith("_")
    )
    gen = (
        model
        for model in classes
        if hasattr(model, "__table__")
        if model.__module__ == module.__name__
    )
    for model in gen:
        yield model
