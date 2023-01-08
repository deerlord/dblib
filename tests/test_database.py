import pytest

from dblib import _create_tables, database
from dblib.models._base import Table
from sqlmodel import select

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


@pytest.mark.asyncio
async def test_selects(setup):
    class ModelOne(Table, table=True):
        ...

    class ModelTwo(Table, table=True):
        ...

    await _create_tables()
    model1 = ModelOne()
    model2 = ModelTwo()
    async with database.connection() as db:
        db.add(model1)
        db.add(model2)
        await db.commit()
        await db.refresh(model1)
        await db.refresh(model2)
    statement = select(ModelOne, ModelTwo).where(ModelOne.id == ModelTwo.id)
    results = [row async for row in database.get_all(statement)]
    assert len(results) == 1
    assert isinstance(results[0][0], ModelOne)
    assert isinstance(results[0][1], ModelTwo)
