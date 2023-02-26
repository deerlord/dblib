"""add weather

Revision ID: 7b6e4ed35942
Revises: f57cc50440c7
Create Date: 2023-02-26 12:45:45.479504

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "7b6e4ed35942"
down_revision = "f57cc50440c7"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "weather_alert",
        sa.Column("location_gpscoords_id", sa.Integer(), nullable=False),
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=True),
        sa.Column("created_at", sa.DateTime(), nullable=True),
        sa.Column("noaa_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("type", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("sent", sa.DateTime(), nullable=False),
        sa.Column("effective", sa.DateTime(), nullable=False),
        sa.Column("onset", sa.DateTime(), nullable=False),
        sa.Column("expires", sa.DateTime(), nullable=False),
        sa.Column("ends", sa.DateTime(), nullable=False),
        sa.Column("status", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("messageType", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("category", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("urgency", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("event", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("sender", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("senderName", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("headline", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("description", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("instruction", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("response", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.ForeignKeyConstraint(
            ["location_gpscoords_id"],
            ["location_gpscoords.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_weather_alert_id"), "weather_alert", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_weather_alert_id"), table_name="weather_alert")
    op.drop_table("weather_alert")
    # ### end Alembic commands ###
