import pytest

from dblib import _create_tables, database
from dblib.models._base import Table

from . import setup


@pytest.mark.asyncio
async def test_database(setup):
    class TestModel(Table, table=True):
        ...

    model = TestModel()
    assert model.id is None

    await _create_tables()
    async with database.connection() as db:
        db.add(model)
        await db.commit()
        await db.refresh(model)

    assert model.id == 1
