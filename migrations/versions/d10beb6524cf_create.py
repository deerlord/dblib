"""create

Revision ID: d10beb6524cf
Revises: 
Create Date: 2023-02-13 18:13:52.295577

"""
import csv
from typing import Iterator
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'd10beb6524cf'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    npkdata = op.create_table('compost_npkdata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('nitrogen', sa.Float(), nullable=False),
    sa.Column('phosphorus', sa.Float(), nullable=False),
    sa.Column('potassium', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_compost_npkdata_id'), 'compost_npkdata', ['id'], unique=False)
    schedule = op.create_table('garden_scheduledata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('germinated', sa.Interval(), nullable=False),
    sa.Column('planted', sa.Interval(), nullable=False),
    sa.Column('harvested', sa.Interval(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_garden_scheduledata_id'), 'garden_scheduledata', ['id'], unique=False)
    op.create_table('garden_stage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.Column('at', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_garden_stage_id'), 'garden_stage', ['id'], unique=False)
    item = op.create_table('inventory_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inventory_item_id'), 'inventory_item', ['id'], unique=False)
    op.create_index(op.f('ix_inventory_item_type'), 'inventory_item', ['type'], unique=False)
    gpscoords = op.create_table('location_gpscoords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('elevation', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('latitude', 'longitude', 'elevation')
    )
    op.create_index(op.f('ix_location_gpscoords_id'), 'location_gpscoords', ['id'], unique=False)
    op.create_table('mqtt_message',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('topic', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('payload', sa.LargeBinary(), nullable=False),
    sa.Column('acked', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_mqtt_message_id'), 'mqtt_message', ['id'], unique=False)
    op.create_table('pantry_container',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('units', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pantry_container_id'), 'pantry_container', ['id'], unique=False)
    op.create_table('sensors_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=False),
    sa.Column('uuid', sqlmodel.sql.sqltypes.GUID(), nullable=False),
    sa.Column('measurement', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('value', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sensors_data_id'), 'sensors_data', ['id'], unique=False)
    op.create_index(op.f('ix_sensors_data_measurement'), 'sensors_data', ['measurement'], unique=False)
    op.create_index(op.f('ix_sensors_data_uuid'), 'sensors_data', ['uuid'], unique=False)
    op.create_table('garden_raisedbed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('gpscoords_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['gpscoords_id'], ['location_gpscoords.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_garden_raisedbed_id'), 'garden_raisedbed', ['id'], unique=False)
    op.create_table('inventory_acquired',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('location', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['inventory_item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inventory_acquired_id'), 'inventory_acquired', ['id'], unique=False)
    op.create_table('inventory_liquidated',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('location', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['inventory_item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inventory_liquidated_id'), 'inventory_liquidated', ['id'], unique=False)
    op.create_table('pantry_stockedgood',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('container_id', sa.Integer(), nullable=False),
    sa.Column('packed', sa.DateTime(), nullable=False),
    sa.Column('expires', sa.DateTime(), nullable=False),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['container_id'], ['pantry_container.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['inventory_item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pantry_stockedgood_id'), 'pantry_stockedgood', ['id'], unique=False)
    op.create_table('sensors_sensor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('gpscoords_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['gpscoords_id'], ['location_gpscoords.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['inventory_item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sensors_sensor_id'), 'sensors_sensor', ['id'], unique=False)
    op.create_table('tasks_action',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('due_by', sa.DateTime(), nullable=True),
    sa.Column('completed', sa.DateTime(), nullable=True),
    sa.Column('category', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['inventory_item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tasks_action_id'), 'tasks_action', ['id'], unique=False)
    op.create_table('weather_forecast',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('gpscoords_id', sa.Integer(), nullable=False),
    sa.Column('start_time', sa.DateTime(), nullable=False),
    sa.Column('end_time', sa.DateTime(), nullable=False),
    sa.Column('is_daytime', sa.Boolean(), nullable=False),
    sa.Column('temperature', sa.Integer(), nullable=False),
    sa.Column('temperature_unit', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('probability_of_precipitation', sa.Float(), nullable=True),
    sa.Column('dewpoint', sa.Float(), nullable=True),
    sa.Column('relative_humidity', sa.Float(), nullable=True),
    sa.Column('wind_speed', sqlmodel.sql.sqltypes.AutoString(), nullable=True),
    sa.Column('wind_direction', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('icon', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('short_forecast', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('detailed_forecast', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['gpscoords_id'], ['location_gpscoords.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('gpscoords_id', 'start_time', 'end_time')
    )
    op.create_index(op.f('ix_weather_forecast_id'), 'weather_forecast', ['id'], unique=False)
    op.create_table('garden_crop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('raisedbed_id', sa.Integer(), nullable=False),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.Column('germinated_id', sa.Integer(), nullable=True),
    sa.Column('planted_id', sa.Integer(), nullable=True),
    sa.Column('harvested_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['germinated_id'], ['garden_stage.id'], ),
    sa.ForeignKeyConstraint(['harvested_id'], ['garden_stage.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['inventory_item.id'], ),
    sa.ForeignKeyConstraint(['planted_id'], ['garden_stage.id'], ),
    sa.ForeignKeyConstraint(['raisedbed_id'], ['garden_raisedbed.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_garden_crop_id'), 'garden_crop', ['id'], unique=False)
    op.create_table('pantry_openedgood',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('stockedgood_id', sa.Integer(), nullable=True),
    sa.Column('opened', sa.DateTime(), nullable=False),
    sa.Column('percent', sa.Float(), nullable=False),
    sa.Column('emptied', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['stockedgood_id'], ['pantry_stockedgood.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_pantry_openedgood_id'), 'pantry_openedgood', ['id'], unique=False)
    op.create_table('tracker_location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('sensor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['inventory_item.id'], ),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensors_sensor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_tracker_location_id'), 'tracker_location', ['id'], unique=False)
    # ### end Alembic commands ###
    data = (
        ("npk", npkdata),
        ("schedule", schedule),
        ("items", item),
        ("gpscoords", gpscoords)
    )
    for name, model in data:
        filename = f"./migrations/data/{name}.csv"
        gen = _csv_data(filename)
        op.bulk_insert(model, list(gen))


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_tracker_location_id'), table_name='tracker_location')
    op.drop_table('tracker_location')
    op.drop_index(op.f('ix_pantry_openedgood_id'), table_name='pantry_openedgood')
    op.drop_table('pantry_openedgood')
    op.drop_index(op.f('ix_garden_crop_id'), table_name='garden_crop')
    op.drop_table('garden_crop')
    op.drop_index(op.f('ix_weather_forecast_id'), table_name='weather_forecast')
    op.drop_table('weather_forecast')
    op.drop_index(op.f('ix_tasks_action_id'), table_name='tasks_action')
    op.drop_table('tasks_action')
    op.drop_index(op.f('ix_sensors_sensor_id'), table_name='sensors_sensor')
    op.drop_table('sensors_sensor')
    op.drop_index(op.f('ix_pantry_stockedgood_id'), table_name='pantry_stockedgood')
    op.drop_table('pantry_stockedgood')
    op.drop_index(op.f('ix_inventory_liquidated_id'), table_name='inventory_liquidated')
    op.drop_table('inventory_liquidated')
    op.drop_index(op.f('ix_inventory_acquired_id'), table_name='inventory_acquired')
    op.drop_table('inventory_acquired')
    op.drop_index(op.f('ix_garden_raisedbed_id'), table_name='garden_raisedbed')
    op.drop_table('garden_raisedbed')
    op.drop_index(op.f('ix_sensors_data_uuid'), table_name='sensors_data')
    op.drop_index(op.f('ix_sensors_data_measurement'), table_name='sensors_data')
    op.drop_index(op.f('ix_sensors_data_id'), table_name='sensors_data')
    op.drop_table('sensors_data')
    op.drop_index(op.f('ix_pantry_container_id'), table_name='pantry_container')
    op.drop_table('pantry_container')
    op.drop_index(op.f('ix_mqtt_message_id'), table_name='mqtt_message')
    op.drop_table('mqtt_message')
    op.drop_index(op.f('ix_location_gpscoords_id'), table_name='location_gpscoords')
    op.drop_table('location_gpscoords')
    op.drop_index(op.f('ix_inventory_item_type'), table_name='inventory_item')
    op.drop_index(op.f('ix_inventory_item_id'), table_name='inventory_item')
    op.drop_table('inventory_item')
    op.drop_index(op.f('ix_garden_stage_id'), table_name='garden_stage')
    op.drop_table('garden_stage')
    op.drop_index(op.f('ix_garden_scheduledata_id'), table_name='garden_scheduledata')
    op.drop_table('garden_scheduledata')
    op.drop_index(op.f('ix_compost_npkdata_id'), table_name='compost_npkdata')
    op.drop_table('compost_npkdata')
    # ### end Alembic commands ###


def _csv_data(filename: str) -> Iterator[dict]:
    with open(filename) as handle:
        reader = csv.reader(handle)
        header = next(reader)
        for row in reader:
            data = dict(zip(header, row))
            yield data