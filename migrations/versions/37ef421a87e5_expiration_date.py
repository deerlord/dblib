"""expiration date

Revision ID: 37ef421a87e5
Revises: b266a7f0f0d6
Create Date: 2023-03-12 04:56:49.675644

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "37ef421a87e5"
down_revision = "b266a7f0f0d6"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "pantry_goodfact", sa.Column("expiration_data", sa.DateTime(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("pantry_goodfact", "expiration_data")
    # ### end Alembic commands ###