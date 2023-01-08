import os

import pytest


@pytest.fixture
def setup():
    filename = "./data.sqlite"
    if os.path.exists(filename):
        os.remove(filename)
    yield
    os.remove(filename)
