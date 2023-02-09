import importlib
import os
import pkgutil
from types import ModuleType
from typing import Iterator, Type

from sqlmodel import SQLModel

from . import models


def find_packages() -> Iterator[ModuleType]:
    pkgpath = os.path.dirname(models.__file__)
    for _, name, _ in pkgutil.iter_modules([pkgpath]):
        if not name.startswith("_"):
            module = importlib.import_module(f"dblib.models.{name}")
            yield module


def find_data_models(package: ModuleType) -> Iterator[Type[SQLModel]]:
    trimmed = (
        getattr(package, model) for model in dir(package) if not model.startswith("_")
    )
    return filter(
        lambda m: m.__module__ == package.__name__,
        filter(lambda m: hasattr(m, "__table__"), trimmed),
    )


def data_models() -> dict[str, list[Type[SQLModel]]]:
    data = {}
    for package in find_packages():
        data = {package.__name__: list(find_data_models(package))}
    return data
