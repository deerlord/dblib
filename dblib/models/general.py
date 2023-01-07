from ._base import Table


class Item(Table, table=True):
    name: str
