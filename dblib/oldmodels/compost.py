from ._base import Base


class NPKData(Base, table=True):
    name: str
    nitrogen: float
    phosphorus: float
    potassium: float
