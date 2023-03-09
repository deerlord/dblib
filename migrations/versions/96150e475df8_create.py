"""create

Revision ID: 96150e475df8
Revises: 
Create Date: 2023-03-07 16:31:24.845292

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "96150e475df8"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "compost_npkdata",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("nitrogen", sa.Float(), nullable=False),
        sa.Column("phosphorus", sa.Float(), nullable=False),
        sa.Column("potassium", sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_compost_npkdata_uuid"), "compost_npkdata", ["uuid"], unique=False
    )
    op.create_table(
        "garden_growthschedule",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("germinate", sa.Interval(), nullable=False),
        sa.Column("plant", sa.Interval(), nullable=False),
        sa.Column("harvest", sa.Interval(), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_garden_growthschedule_uuid"),
        "garden_growthschedule",
        ["uuid"],
        unique=False,
    )
    op.create_table(
        "garden_irrigationhose",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("type", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("emitters_per_foot", sa.Float(), nullable=False),
        sa.Column("gallons_per_hour", sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
        sa.UniqueConstraint("type", "emitters_per_foot", "gallons_per_hour"),
    )
    op.create_index(
        op.f("ix_garden_irrigationhose_uuid"),
        "garden_irrigationhose",
        ["uuid"],
        unique=False,
    )
    op.create_table(
        "garden_wateringschedule",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("gallons", sa.Float(), nullable=False),
        sa.Column("period", sa.Interval(), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_garden_wateringschedule_uuid"),
        "garden_wateringschedule",
        ["uuid"],
        unique=False,
    )
    op.create_table(
        "inventory_item",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("type", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_inventory_item_type"), "inventory_item", ["type"], unique=False
    )
    op.create_index(
        op.f("ix_inventory_item_uuid"), "inventory_item", ["uuid"], unique=False
    )
    op.create_table(
        "location_gpscoords",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("latitude", sa.Float(), nullable=False),
        sa.Column("longitude", sa.Float(), nullable=False),
        sa.Column("elevation", sa.Float(), nullable=True),
        sa.PrimaryKeyConstraint("uuid"),
        sa.UniqueConstraint("latitude", "longitude", "elevation"),
    )
    op.create_index(
        op.f("ix_location_gpscoords_uuid"), "location_gpscoords", ["uuid"], unique=False
    )
    op.create_table(
        "location_polygon",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_location_polygon_uuid"), "location_polygon", ["uuid"], unique=False
    )
    op.create_table(
        "pantry_container",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("units", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("size", sa.Float(), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_pantry_container_uuid"), "pantry_container", ["uuid"], unique=False
    )
    op.create_table(
        "garden_irrigationgrid",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column(
            "garden_irrigationhose_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False
        ),
        sa.Column("count", sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(
            ["garden_irrigationhose_uuid"],
            ["garden_irrigationhose.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_garden_irrigationgrid_uuid"),
        "garden_irrigationgrid",
        ["uuid"],
        unique=False,
    )
    op.create_table(
        "garden_plant",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("inventory_item_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("compost_npkdata_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column(
            "garden_growthschedule_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False
        ),
        sa.Column(
            "garden_wateringschedule_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["compost_npkdata_uuid"],
            ["compost_npkdata.uuid"],
        ),
        sa.ForeignKeyConstraint(
            ["garden_growthschedule_uuid"],
            ["garden_growthschedule.uuid"],
        ),
        sa.ForeignKeyConstraint(
            ["garden_wateringschedule_uuid"],
            ["garden_wateringschedule.uuid"],
        ),
        sa.ForeignKeyConstraint(
            ["inventory_item_uuid"],
            ["inventory_item.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_garden_plant_uuid"), "garden_plant", ["uuid"], unique=False
    )
    op.create_table(
        "location_linktable",
        sa.Column(
            "location_polygon_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False
        ),
        sa.Column(
            "location_gpscoords_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["location_gpscoords_uuid"],
            ["location_gpscoords.uuid"],
        ),
        sa.ForeignKeyConstraint(
            ["location_polygon_uuid"],
            ["location_polygon.uuid"],
        ),
        sa.PrimaryKeyConstraint("location_polygon_uuid", "location_gpscoords_uuid"),
    )
    op.create_table(
        "pantry_good",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("inventory_item_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column(
            "pantry_container_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False
        ),
        sa.ForeignKeyConstraint(
            ["inventory_item_uuid"],
            ["inventory_item.uuid"],
        ),
        sa.ForeignKeyConstraint(
            ["pantry_container_uuid"],
            ["pantry_container.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(op.f("ix_pantry_good_uuid"), "pantry_good", ["uuid"], unique=False)
    op.create_table(
        "weather_alert",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column(
            "location_gpscoords_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False
        ),
        sa.Column("noaa_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("sent", sa.DateTime(), nullable=False),
        sa.Column("effective", sa.DateTime(), nullable=False),
        sa.Column("onset", sa.DateTime(), nullable=True),
        sa.Column("expires", sa.DateTime(), nullable=False),
        sa.Column("ends", sa.DateTime(), nullable=True),
        sa.Column("status", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("message_type", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("category", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("urgency", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("event", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("sender", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("sender_name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("headline", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("description", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("instruction", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("response", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.ForeignKeyConstraint(
            ["location_gpscoords_uuid"],
            ["location_gpscoords.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
        sa.UniqueConstraint("noaa_id"),
    )
    op.create_index(
        op.f("ix_weather_alert_uuid"), "weather_alert", ["uuid"], unique=False
    )
    op.create_table(
        "garden_bed",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column(
            "location_polygon_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False
        ),
        sa.Column(
            "garden_irrigationgrid_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=True
        ),
        sa.Column("width", sa.Float(), nullable=False),
        sa.Column("length", sa.Float(), nullable=False),
        sa.Column("height", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(
            ["garden_irrigationgrid_uuid"],
            ["garden_irrigationgrid.uuid"],
        ),
        sa.ForeignKeyConstraint(
            ["location_polygon_uuid"],
            ["location_polygon.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(op.f("ix_garden_bed_uuid"), "garden_bed", ["uuid"], unique=False)
    op.create_table(
        "pantry_consumed",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("pantry_good_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("at", sa.DateTime(), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("unit", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.ForeignKeyConstraint(
            ["pantry_good_uuid"],
            ["pantry_good.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_pantry_consumed_uuid"), "pantry_consumed", ["uuid"], unique=False
    )
    op.create_table(
        "pantry_stocked",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("pantry_good_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("at", sa.DateTime(), nullable=False),
        sa.Column("count", sa.Integer(), nullable=False),
        sa.Column("expires", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["pantry_good_uuid"],
            ["pantry_good.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_pantry_stocked_uuid"), "pantry_stocked", ["uuid"], unique=False
    )
    op.create_table(
        "garden_crop",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("garden_bed_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("garden_plant_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("count", sa.Integer(), nullable=True),
        sa.Column("planted", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["garden_bed_uuid"],
            ["garden_bed.uuid"],
        ),
        sa.ForeignKeyConstraint(
            ["garden_plant_uuid"],
            ["garden_plant.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(op.f("ix_garden_crop_uuid"), "garden_crop", ["uuid"], unique=False)
    op.create_table(
        "garden_harvest",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("garden_crop_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("count", sa.Integer(), nullable=False),
        sa.Column("weight", sa.Float(), nullable=False),
        sa.ForeignKeyConstraint(
            ["garden_crop_uuid"],
            ["garden_crop.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_garden_harvest_uuid"), "garden_harvest", ["uuid"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_garden_harvest_uuid"), table_name="garden_harvest")
    op.drop_table("garden_harvest")
    op.drop_index(op.f("ix_garden_crop_uuid"), table_name="garden_crop")
    op.drop_table("garden_crop")
    op.drop_index(op.f("ix_pantry_stocked_uuid"), table_name="pantry_stocked")
    op.drop_table("pantry_stocked")
    op.drop_index(op.f("ix_pantry_consumed_uuid"), table_name="pantry_consumed")
    op.drop_table("pantry_consumed")
    op.drop_index(op.f("ix_garden_bed_uuid"), table_name="garden_bed")
    op.drop_table("garden_bed")
    op.drop_index(op.f("ix_weather_alert_uuid"), table_name="weather_alert")
    op.drop_table("weather_alert")
    op.drop_index(op.f("ix_pantry_good_uuid"), table_name="pantry_good")
    op.drop_table("pantry_good")
    op.drop_table("location_linktable")
    op.drop_index(op.f("ix_garden_plant_uuid"), table_name="garden_plant")
    op.drop_table("garden_plant")
    op.drop_index(
        op.f("ix_garden_irrigationgrid_uuid"), table_name="garden_irrigationgrid"
    )
    op.drop_table("garden_irrigationgrid")
    op.drop_index(op.f("ix_pantry_container_uuid"), table_name="pantry_container")
    op.drop_table("pantry_container")
    op.drop_index(op.f("ix_location_polygon_uuid"), table_name="location_polygon")
    op.drop_table("location_polygon")
    op.drop_index(op.f("ix_location_gpscoords_uuid"), table_name="location_gpscoords")
    op.drop_table("location_gpscoords")
    op.drop_index(op.f("ix_inventory_item_uuid"), table_name="inventory_item")
    op.drop_index(op.f("ix_inventory_item_type"), table_name="inventory_item")
    op.drop_table("inventory_item")
    op.drop_index(
        op.f("ix_garden_wateringschedule_uuid"), table_name="garden_wateringschedule"
    )
    op.drop_table("garden_wateringschedule")
    op.drop_index(
        op.f("ix_garden_irrigationhose_uuid"), table_name="garden_irrigationhose"
    )
    op.drop_table("garden_irrigationhose")
    op.drop_index(
        op.f("ix_garden_growthschedule_uuid"), table_name="garden_growthschedule"
    )
    op.drop_table("garden_growthschedule")
    op.drop_index(op.f("ix_compost_npkdata_uuid"), table_name="compost_npkdata")
    op.drop_table("compost_npkdata")
    # ### end Alembic commands ###