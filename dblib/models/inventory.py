from ._base import Base


class ItemDimension(Base, table=True):
    name: str
