from dblib import database
from sqlmodel import select
import os
import csv
import asyncio


async def main():
    for package_name, models in database.data_models().items():
        dirpath = f"csv_data/{package_name}"
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        for model in models:
            statement = select(model)
            filename = f"{dirpath}/{model.__name__}.csv"
            async with database.connection() as conn:
                results = await conn.execute(statement)
                lines = results.scalars().all()
            if len(lines) == 0:
                continue
            with open(filename, "w") as handle:
                headers = lines[0].__fields__.keys()
                writer = csv.DictWriter(handle, fieldnames=headers)
                writer.writeheader()
                gen = (
                    line.dict()
                    for line in lines
                )
                writer.writerows(gen)


if __name__ == "__main__":
    asyncio.run(main())