import asyncio
from . import database
from sqlmodel import SQLModel


async def create_tables():
    local = database.engine()
    async with local.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)


if __name__ == "__main__":
    asyncio.run(create_tables())
