from contextlib import asynccontextmanager
from typing import AsyncGenerator, TypeAlias, TypeVar

from sqlalchemy.ext.asyncio import AsyncEngine, AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from .settings import Settings

settings = Settings()
if settings.database_protocol == "sqlite":
    from sqlite3 import IntegrityError as DBError
elif settings.database_protocol == "postgres":
    from asyncpg.exceptions import PostgresError as DBError  # type: ignore

T = TypeVar("T")
__all__ = ["engine", "connection"]

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


@asynccontextmanager
async def connection() -> AsyncGenerator[SESSION, None]:
    async with session() as local:
        try:
            yield local
            await local.commit()
        except DBError:
            await local.rollback()


session = sessionmaker(engine(), expire_on_commit=False, class_=SESSION)
