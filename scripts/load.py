import asyncio
import csv
import sys
from typing import Type

from sqlmodel import SQLModel

from dblib import database


async def main():
    topdir = sys.argv[1]
    for package_name, models in database.data_models().items():
        dirpath = f"{topdir}/{package_name}"
        for model in models:
            await _insert(dirpath, model)


async def _insert(dirpath: str, model: Type[SQLModel]):
    filename = f"{dirpath}/{model.__name__}.csv"
    with open(filename, "r") as handle:
        reader = csv.DictReader(handle)
        instances = (model(**row) for row in reader)
        async with database.connection() as conn:
            for instance in instances:
                conn.add(instance)


if __name__ == "__main__":
    asyncio.run(main())
