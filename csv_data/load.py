import asyncio
from dblib import models, database
import csv
from sqlmodel import SQLModel

# filename, model
getters = (
    ("schedule.csv", models.garden.ScheduleData),
    ("npk.csv", models.compost.NPKData),
    ("items.csv", models.inventory.Item),
)

def main():
    for filename, model in getters:
        with open(filename, "r") as handle:
            reader = csv.reader(handle)
            header = reader[0]
            do = work(model, header, reader[1:])
            asyncio.run(do)


async def work(model: SQLModel, header: list, rows: list):
    for row in rows[1:]:
        data = dict(zip(header, row))
        instance = model(**data)
        async with database.connection() as conn:
            conn.add(instance)
            conn.commit()
