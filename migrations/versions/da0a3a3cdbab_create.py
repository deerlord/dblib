"""create

Revision ID: da0a3a3cdbab
Revises: 
Create Date: 2023-02-09 00:51:54.850142

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'da0a3a3cdbab'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('compost_npkdata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('nitrogen', sa.Float(), nullable=False),
    sa.Column('phosphorus', sa.Float(), nullable=False),
    sa.Column('potassium', sa.Float(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('garden_scheduledata',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('germinated', sa.Interval(), nullable=False),
    sa.Column('planted', sa.Interval(), nullable=False),
    sa.Column('harvested', sa.Interval(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inventory_item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('type', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_inventory_item_type'), 'inventory_item', ['type'], unique=False)
    gpscoords = op.create_table('location_gpscoords',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('latitude', sa.Float(), nullable=False),
    sa.Column('longitude', sa.Float(), nullable=False),
    sa.Column('elevation', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pantry_container',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('units', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('size', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('garden_raisedbed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('gpscoords_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['gpscoords_id'], ['location_gpscoords.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inventory_acquired',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('location', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['inventory_item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('inventory_liquidated',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('date', sa.DateTime(), nullable=False),
    sa.Column('location', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['inventory_item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pantry_stockedgood',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('container_id', sa.Integer(), nullable=False),
    sa.Column('packed', sa.DateTime(), nullable=False),
    sa.Column('expires', sa.DateTime(), nullable=False),
    sa.Column('count', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['container_id'], ['pantry_container.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['inventory_item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('sensors_sensor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('gpscoords_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['gpscoords_id'], ['location_gpscoords.id'], ),
    sa.ForeignKeyConstraint(['item_id'], ['inventory_item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks_action',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('description', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('due_by', sa.DateTime(), nullable=True),
    sa.Column('completed', sa.DateTime(), nullable=True),
    sa.Column('category', sqlmodel.sql.sqltypes.AutoString(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['inventory_item.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('garden_plant',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('raisedbed_id', sa.Integer(), nullable=False),
    sa.Column('germinated', sa.DateTime(), nullable=True),
    sa.Column('planted', sa.DateTime(), nullable=True),
    sa.Column('harvested', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['item_id'], ['inventory_item.id'], ),
    sa.ForeignKeyConstraint(['raisedbed_id'], ['garden_raisedbed.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('pantry_openedgood',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stockedgood_id', sa.Integer(), nullable=True),
    sa.Column('opened', sa.DateTime(), nullable=False),
    sa.Column('percent', sa.Float(), nullable=False),
    sa.Column('emptied', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['stockedgood_id'], ['pantry_stockedgood.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tasks_block',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('blocker_id', sa.Integer(), nullable=False),
    sa.Column('blocked_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['blocked_id'], ['tasks_action.id'], ),
    sa.ForeignKeyConstraint(['blocker_id'], ['tasks_action.id'], ),
    sa.PrimaryKeyConstraint('id', 'blocker_id', 'blocked_id')
    )
    op.create_table('tracker_location',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time', sa.DateTime(), nullable=False),
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('sensor_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['item_id'], ['inventory_item.id'], ),
    sa.ForeignKeyConstraint(['sensor_id'], ['sensors_sensor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.bulk_insert(gpscoords, [{"latitude": 0.0, "longitude": 0.0}])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tracker_location')
    op.drop_table('tasks_block')
    op.drop_table('pantry_openedgood')
    op.drop_table('garden_plant')
    op.drop_table('tasks_action')
    op.drop_table('sensors_sensor')
    op.drop_table('pantry_stockedgood')
    op.drop_table('inventory_liquidated')
    op.drop_table('inventory_acquired')
    op.drop_table('garden_raisedbed')
    op.drop_table('pantry_container')
    op.drop_table('location_gpscoords')
    op.drop_index(op.f('ix_inventory_item_type'), table_name='inventory_item')
    op.drop_table('inventory_item')
    op.drop_table('garden_scheduledata')
    op.drop_table('compost_npkdata')
    # ### end Alembic commands ###