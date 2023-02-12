"""weather_forecast

Revision ID: abc2f7c2e3c8
Revises: da0a3a3cdbab
Create Date: 2023-02-11 23:48:00.339127

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'abc2f7c2e3c8'
down_revision = 'da0a3a3cdbab'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('weather_forecast',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('startTime', sa.DateTime(), nullable=False),
    sa.Column('endTime', sa.DateTime(), nullable=False),
    sa.Column('isDaytime', sa.Boolean(), nullable=False),
    sa.Column('temperature', sa.Integer(), nullable=False),
    sa.Column('temperatureUnit', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('probabilityOfPrecipitation', sa.Float(), nullable=True),
    sa.Column('dewpoint', sa.Float(), nullable=True),
    sa.Column('relativeHumidity', sa.Float(), nullable=True),
    sa.Column('windspeed', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('windDirection', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('icon', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('shortForecast', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('detailedForecast', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('weather_forecast')
    # ### end Alembic commands ###
