"""remove_null

Revision ID: 1913b1bf9b7e
Revises: 6684d5ef7f11
Create Date: 2023-02-08 22:50:33.730072

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "1913b1bf9b7e"
down_revision = "6684d5ef7f11"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "sensors_sensor", "item_id", existing_type=sa.INTEGER(), nullable=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "sensors_sensor", "item_id", existing_type=sa.INTEGER(), nullable=True
    )
    # ### end Alembic commands ###
