"""create

Revision ID: b266a7f0f0d6
Revises: 
Create Date: 2023-03-12 04:48:07.825107

"""
from alembic import op
import sqlalchemy as sa
import sqlmodel


# revision identifiers, used by Alembic.
revision = "b266a7f0f0d6"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "inventory_itemdimension",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_inventory_itemdimension_uuid"),
        "inventory_itemdimension",
        ["uuid"],
        unique=False,
    )
    op.create_table(
        "pantry_containerdimension",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("type", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("size", sa.Float(), nullable=False),
        sa.Column("units", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_pantry_containerdimension_uuid"),
        "pantry_containerdimension",
        ["uuid"],
        unique=False,
    )
    op.create_table(
        "pantry_goodfact",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column(
            "inventory_itemdimension_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False
        ),
        sa.Column(
            "pantry_containerdimension_uuid",
            sqlmodel.sql.sqltypes.GUID(),
            nullable=False,
        ),
        sa.ForeignKeyConstraint(
            ["inventory_itemdimension_uuid"],
            ["inventory_itemdimension.uuid"],
        ),
        sa.ForeignKeyConstraint(
            ["pantry_containerdimension_uuid"],
            ["pantry_containerdimension.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_pantry_goodfact_inventory_itemdimension_uuid"),
        "pantry_goodfact",
        ["inventory_itemdimension_uuid"],
        unique=False,
    )
    op.create_index(
        op.f("ix_pantry_goodfact_pantry_containerdimension_uuid"),
        "pantry_goodfact",
        ["pantry_containerdimension_uuid"],
        unique=False,
    )
    op.create_index(
        op.f("ix_pantry_goodfact_uuid"), "pantry_goodfact", ["uuid"], unique=False
    )
    op.create_table(
        "pantry_actionfact",
        sa.Column("uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.Column("pantry_goodfact_uuid", sqlmodel.sql.sqltypes.GUID(), nullable=False),
        sa.Column("action", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("amount", sa.Float(), nullable=False),
        sa.Column("units", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("at", sa.DateTime(), nullable=False),
        sa.ForeignKeyConstraint(
            ["pantry_goodfact_uuid"],
            ["pantry_goodfact.uuid"],
        ),
        sa.PrimaryKeyConstraint("uuid"),
    )
    op.create_index(
        op.f("ix_pantry_actionfact_pantry_goodfact_uuid"),
        "pantry_actionfact",
        ["pantry_goodfact_uuid"],
        unique=False,
    )
    op.create_index(
        op.f("ix_pantry_actionfact_uuid"), "pantry_actionfact", ["uuid"], unique=False
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_pantry_actionfact_uuid"), table_name="pantry_actionfact")
    op.drop_index(
        op.f("ix_pantry_actionfact_pantry_goodfact_uuid"),
        table_name="pantry_actionfact",
    )
    op.drop_table("pantry_actionfact")
    op.drop_index(op.f("ix_pantry_goodfact_uuid"), table_name="pantry_goodfact")
    op.drop_index(
        op.f("ix_pantry_goodfact_pantry_containerdimension_uuid"),
        table_name="pantry_goodfact",
    )
    op.drop_index(
        op.f("ix_pantry_goodfact_inventory_itemdimension_uuid"),
        table_name="pantry_goodfact",
    )
    op.drop_table("pantry_goodfact")
    op.drop_index(
        op.f("ix_pantry_containerdimension_uuid"),
        table_name="pantry_containerdimension",
    )
    op.drop_table("pantry_containerdimension")
    op.drop_index(
        op.f("ix_inventory_itemdimension_uuid"), table_name="inventory_itemdimension"
    )
    op.drop_table("inventory_itemdimension")
    # ### end Alembic commands ###
