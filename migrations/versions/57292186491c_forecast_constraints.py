"""forecast_constraints

Revision ID: 57292186491c
Revises: 55aa65d0f940
Create Date: 2023-02-12 02:56:26.457180

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = '57292186491c'
down_revision = '55aa65d0f940'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'weather_forecast', ['gpscoords_id', 'start_time', 'end_time'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'weather_forecast', type_='unique')
    # ### end Alembic commands ###
