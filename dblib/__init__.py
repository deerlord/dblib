import asyncio

from sqlmodel import SQLModel

from . import database


def create_tables():
    asyncio.run(_create_tables())


async def _create_tables():
    local = database.engine()
    async with local.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
