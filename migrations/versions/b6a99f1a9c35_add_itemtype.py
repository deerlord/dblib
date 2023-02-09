"""add_itemtype

Revision ID: b6a99f1a9c35
Revises: 8a4c20a69cef
Create Date: 2023-02-08 22:44:58.370979

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = 'b6a99f1a9c35'
down_revision = '8a4c20a69cef'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('inventory_item', sa.Column('type', sqlmodel.sql.sqltypes.AutoString(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('inventory_item', 'type')
    # ### end Alembic commands ###
