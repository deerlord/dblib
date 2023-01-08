from contextlib import asynccontextmanager
from typing import AsyncGenerator, TypeAlias, TypeVar

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker
from sqlmodel.sql.expression import Select

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
