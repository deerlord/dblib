from ..models._base import Table


class NPKData(Table, table=True):
    name: str
    nitrogen: float
    phosphorus: float
    potassium: float
