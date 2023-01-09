import asyncio
import importlib
import os
import pkgutil
from contextlib import asynccontextmanager
from typing import AsyncGenerator, Type, TypeAlias, TypeVar

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel import SQLModel
from sqlmodel.sql.expression import Select

from . import models
from .settings import Settings

T = TypeVar("T")

settings = Settings()
if settings.database_protocol == "sqlite":
    from sqlite3 import IntegrityError as DBError
elif settings.database_protocol == "postgres":
    from asyncpg.exceptions import PostgresError as DBError  # type: ignore


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
        except DBError:
            await local.rollback()


async def get_all(statement: Select[T]) -> AsyncGenerator[T, None]:  # type: ignore
    async with connection() as db:
        results = await db.execute(statement)
        for result in results.fetchall():
            yield result  # type: ignore


def create_tables():
    asyncio.run(_create_tables())


async def _create_tables():
    local = engine()
    async with local.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


def data_models() -> dict[str, list[Type[SQLModel]]]:
    retval = {}
    pkgpath = os.path.dirname(models.__file__)
    for _, name, _ in pkgutil.iter_modules([pkgpath]):
        if not name.startswith("_"):
            module = importlib.import_module(f"dblib.models.{name}")
            trimmed = (
                getattr(module, model)
                for model in dir(module)
                if not model.startswith("_")
            )
            data = filter(
                lambda m: m.__module__ == module.__name__,
                filter(lambda m: hasattr(m, "__table__"), trimmed),
            )
            retval[name] = list(data)
    return retval
