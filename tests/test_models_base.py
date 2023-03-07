from dblib.models._base import Base


def test_tablename():
    class TestModel(Base):
        ...

    assert TestModel.__tablename__ == "test_models_base_testmodel"
