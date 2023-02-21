import asyncio
import csv
import os
from typing import Type

from sqlmodel import SQLModel

from dblib import database


async def main():
    topdirs = "migrations", "data"
    for package_name, models in database.data_models().items():
        dirpath = os.path.join(*topdirs, package_name)
        for model in models:
            await _load(dirpath, model)


async def _load(dirpath: str, model: Type[SQLModel]):
    filename = f"{dirpath}/{model.__name__}.csv"
    try:
        with open(filename, "r") as handle:
            reader = csv.DictReader(handle)
            instances = (model(**row) for row in reader)
            async with database.connection() as conn:
                for instance in instances:
                    conn.add(instance)
    except:
        pass


if __name__ == "__main__":
    asyncio.run(main())
