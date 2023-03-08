from datetime import datetime, timedelta

from sqlmodel import Field, Relationship, UniqueConstraint

from ..enums import garden
from ._base import TABLE_ID, Base
from .compost import NPKData
from .inventory import Item
from .location import Polygon


class WateringSchedule(Base, table=True):
    gallons: float
    period: timedelta


class GrowthSchedule(Base, table=True):
    germinate: timedelta
    plant: timedelta
    harvest: timedelta


class Plant(Base, table=True):
    inventory_item_uuid: TABLE_ID = Field(foreign_key=f"{Item.__tablename__}.uuid")
    item: Item = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Plant.inventory_item_uuid",
        }
    )
    compost_npkdata_uuid: TABLE_ID = Field(foreign_key=f"{NPKData.__tablename__}.uuid")
    npk: NPKData = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Plant.compost_npkdata_uuid",
        }
    )
    garden_growthschedule_uuid: TABLE_ID = Field(
        foreign_key=f"{GrowthSchedule.__tablename__}.uuid"
    )
    growth_schedule: GrowthSchedule = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Plant.garden_growthschedule_uuid",
        }
    )
    garden_wateringschedule_uuid: TABLE_ID = Field(
        foreign_key=f"{WateringSchedule.__tablename__}.uuid"
    )
    watering_schedule: WateringSchedule = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Plant.garden_wateringschedule_uuid",
        }
    )


class IrrigationHose(Base, table=True):
    __table_args__ = (
        UniqueConstraint("type", "emitters_per_foot", "gallons_per_hour"),
    )
    type: garden.IrrigationHoseType
    emitters_per_foot: float
    gallons_per_hour: float


class IrrigationGrid(Base, table=True):
    garden_irrigationhose_uuid: TABLE_ID = Field(
        foreign_key=f"{IrrigationHose.__tablename__}.uuid"
    )
    hose: IrrigationHose = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "IrrigationGrid.garden_irrigationhose_uuid",
        }
    )
    count: int


class Bed(Base, table=True):
    location_polygon_uuid: TABLE_ID = Field(foreign_key=f"{Polygon.__tablename__}.uuid")
    coords: Polygon = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Bed.location_polygon_uuid",
        }
    )
    garden_irrigationgrid_uuid: TABLE_ID | None = Field(
        foreign_key=f"{IrrigationGrid.__tablename__}.uuid"
    )
    irrigationgrid: IrrigationGrid | None = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Bed.garden_irrigationgrid_uuid",
        }
    )
    width: float
    length: float
    height: float


class Crop(Base, table=True):
    garden_bed_uuid: TABLE_ID = Field(foreign_key=f"{Bed.__tablename__}.uuid")
    bed: Bed = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Crop.garden_bed_uuid",
        }
    )
    garden_plant_uuid: TABLE_ID = Field(foreign_key=f"{Plant.__tablename__}.uuid")
    plant: Plant = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Crop.garden_plant_uuid",
        }
    )
    count: int | None = None
    planted: datetime


class Harvest(Base, table=True):
    garden_crop_uuid: TABLE_ID = Field(foreign_key=f"{Crop.__tablename__}.uuid")
    crop: Crop = Relationship(
        sa_relationship_kwargs={
            "lazy": "selectin",
            "foreign_keys": "Harvest.garden_crop_uuid",
        }
    )
    count: int
    weight: float
