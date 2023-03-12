"""expiration date fixed

Revision ID: 72fd38943f64
Revises: 37ef421a87e5
Create Date: 2023-03-12 04:57:32.472404

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = "72fd38943f64"
down_revision = "37ef421a87e5"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "pantry_goodfact", sa.Column("expiration_date", sa.DateTime(), nullable=True)
    )
    op.drop_column("pantry_goodfact", "expiration_data")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "pantry_goodfact",
        sa.Column(
            "expiration_data",
            postgresql.TIMESTAMP(),
            autoincrement=False,
            nullable=True,
        ),
    )
    op.drop_column("pantry_goodfact", "expiration_date")
    # ### end Alembic commands ###
