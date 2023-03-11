"""pantry and sensors

Revision ID: f0b4afadf04e
Revises: 49b2ea32058b
Create Date: 2023-03-10 19:32:36.005397

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "f0b4afadf04e"
down_revision = "49b2ea32058b"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "sensor_model",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("number", sa.Integer(), nullable=False),
        sa.Column("measurement", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_sensor_model_uuid"), "sensor_model", ["uuid"], unique=False
    )
    op.drop_column("pantry_container", "name")
    op.add_column(
        "pantry_good",
        sa.Column("brand", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    )
    op.add_column(
        "sensor_sensor",
        sa.Column("sensor_model_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
    )
    op.add_column(
        "sensor_sensor",
        sa.Column(
            "location_gpscoords_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=True
        ),
    )
    op.create_foreign_key(
        None,
        "sensor_sensor",
        "location_gpscoords",
        ["location_gpscoords_uuid"],
        ["uuid"],
    )
    op.create_foreign_key(
        None, "sensor_sensor", "sensor_model", ["sensor_model_uuid"], ["uuid"]
    )
    op.drop_column("sensor_sensor", "model")
    op.drop_column("sensor_sensor", "measurement")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "sensor_sensor",
        sa.Column("measurement", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.add_column(
        "sensor_sensor",
        sa.Column("model", sa.INTEGER(), autoincrement=False, nullable=False),
    )
    op.drop_constraint(None, "sensor_sensor", type_="foreignkey")
    op.drop_constraint(None, "sensor_sensor", type_="foreignkey")
    op.drop_column("sensor_sensor", "location_gpscoords_uuid")
    op.drop_column("sensor_sensor", "sensor_model_uuid")
    op.drop_column("pantry_good", "brand")
    op.add_column(
        "pantry_container",
        sa.Column("name", sa.VARCHAR(), autoincrement=False, nullable=False),
    )
    op.drop_index(op.f("ix_sensor_model_uuid"), table_name="sensor_model")
    op.drop_table("sensor_model")
    # ### end Alembic commands ###
