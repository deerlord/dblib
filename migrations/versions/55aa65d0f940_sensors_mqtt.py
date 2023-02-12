"""sensors_mqtt

Revision ID: 55aa65d0f940
Revises: 12886d7c997b
Create Date: 2023-02-12 02:27:36.164942

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '55aa65d0f940'
down_revision = '12886d7c997b'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('mqtt_message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('topic', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('payload', sa.LargeBinary(), nullable=False),
    sa.Column('acked', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sensors_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('uuid', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('measurement', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sensors_data_measurement'), 'sensors_data', ['measurement'], unique=False)
    op.create_index(op.f('ix_sensors_data_uuid'), 'sensors_data', ['uuid'], unique=False)
    op.add_column('weather_forecast', sa.Column('gpscoords_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'weather_forecast', 'location_gpscoords', ['gpscoords_id'], ['id'])
    op.drop_column('weather_forecast', 'longitude')
    op.drop_column('weather_forecast', 'latitude')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('weather_forecast', sa.Column('latitude', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.add_column('weather_forecast', sa.Column('longitude', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'weather_forecast', type_='foreignkey')
    op.drop_column('weather_forecast', 'gpscoords_id')
    op.drop_index(op.f('ix_sensors_data_uuid'), table_name='sensors_data')
    op.drop_index(op.f('ix_sensors_data_measurement'), table_name='sensors_data')
    op.drop_table('sensors_data')
    op.drop_table('mqtt_message')
    # ### end Alembic commands ###
