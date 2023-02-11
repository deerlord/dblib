import asyncio
import csv
import os
from typing import Type

from sqlmodel import SQLModel, select

from dblib import database


async def main():
    for package_name, models in database.data_models().items():
        dirpath = f"csv_data/{package_name}"
        os.makedirs(dirpath)
        for model in models:
            await _save(dirpath, model)


async def _save(dirpath: str, model: Type[SQLModel]):
    filename = f"{dirpath}/{model.__name__}.csv"
    async with database.connection() as conn:
        statement = select(model)
        results = await conn.execute(statement)
        lines = results.scalars().all()
    if len(lines) == 0:
        return
    with open(filename, "w") as handle:
        headers = lines[0].__fields__.keys()
        writer = csv.DictWriter(handle, fieldnames=headers)
        writer.writeheader()
        gen = (line.dict() for line in lines)
        writer.writerows(gen)


if __name__ == "__main__":
    asyncio.run(main())
