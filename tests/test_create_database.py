from dblib import create_tables
import os
from dblib.settings import Settings


def test_create_tables():
    filename = "tests/data.sqlite"
    os.environ["DBLIB_NAME"] = f"/{filename}"
    os.environ["DBLIB_PROTOCAL"] = "sqlite"
    if os.path.exists(filename):
        os.remove(filename)
    create_tables()
    os.remove(filename)
