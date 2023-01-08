from dblib.models._base import Table


def test_tablename():
    class TestModel(Table):
        ...

    assert TestModel.__tablename__ == "test_models_base_testmodel"
