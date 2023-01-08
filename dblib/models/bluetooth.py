from ._base import Table


class Device(Table, table=True):
    name: str
