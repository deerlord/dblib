"""ingredient_to_item

Revision ID: 5f2fdf48aec5
Revises: 7e58458313a1
Create Date: 2023-02-09 00:29:58.263719

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "5f2fdf48aec5"
down_revision = "7e58458313a1"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "pantry_stockedgood", sa.Column("item_id", sa.Integer(), nullable=False)
    )
    op.alter_column(
        "pantry_stockedgood", "container_id", existing_type=sa.INTEGER(), nullable=False
    )
    op.drop_constraint(
        "pantry_stockedgood_ingredient_id_fkey",
        "pantry_stockedgood",
        type_="foreignkey",
    )
    op.create_foreign_key(
        None, "pantry_stockedgood", "inventory_item", ["item_id"], ["id"]
    )
    op.drop_column("pantry_stockedgood", "ingredient_id")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "pantry_stockedgood",
        sa.Column("ingredient_id", sa.INTEGER(), autoincrement=False, nullable=True),
    )
    op.drop_constraint(None, "pantry_stockedgood", type_="foreignkey")
    op.create_foreign_key(
        "pantry_stockedgood_ingredient_id_fkey",
        "pantry_stockedgood",
        "inventory_item",
        ["ingredient_id"],
        ["id"],
    )
    op.alter_column(
        "pantry_stockedgood", "container_id", existing_type=sa.INTEGER(), nullable=True
    )
    op.drop_column("pantry_stockedgood", "item_id")
    # ### end Alembic commands ###
