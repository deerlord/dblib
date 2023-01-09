import os

import pytest


@pytest.fixture
def setup():
    filename = "data.sqlite"
    if os.path.exists(filename):
        os.remove(filename)
    try:
        yield
    except:
        ...
    os.remove(filename)
