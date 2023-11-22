"""Add index ID and host

Revision ID: e83263a5def4
Revises: 826abb0c4222
Create Date: 2023-02-13 15:58:55.102285

"""
import sqlalchemy as sa
import sqlmodel  # noqa: F401
from alembic import op

# revision identifiers, used by Alembic.
revision = "e83263a5def4"
down_revision = "826abb0c4222"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column(
        "apiecoindex", "id", existing_type=sqlmodel.sql.sqltypes.GUID(), nullable=False
    )
    op.alter_column(
        "apiecoindex", "version", existing_type=sa.INTEGER(), nullable=False
    )
    op.create_index(op.f("ix_apiecoindex_host"), "apiecoindex", ["host"], unique=False)
    op.create_index(op.f("ix_apiecoindex_id"), "apiecoindex", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_apiecoindex_id"), table_name="apiecoindex")
    op.drop_index(op.f("ix_apiecoindex_host"), table_name="apiecoindex")
    op.alter_column("apiecoindex", "version", existing_type=sa.INTEGER(), nullable=True)
    op.alter_column(
        "apiecoindex", "id", existing_type=sqlmodel.sql.sqltypes.GUID(), nullable=True
    )
    # ### end Alembic commands ###
