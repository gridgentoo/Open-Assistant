"""Add worker compliance checks to db

Revision ID: a2865908a537
Revises: e7a4bffb424c
Create Date: 2023-02-26 13:28:25.181340

"""
import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision = "a2865908a537"
down_revision = "e7a4bffb424c"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "worker_compliance_check",
        sa.Column("id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("worker_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("compare_worker_id", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("start_time", sa.DateTime(), nullable=False),
        sa.Column("end_time", sa.DateTime(), nullable=True),
        sa.Column("responded", sa.Boolean(), nullable=False),
        sa.Column("error", sqlmodel.sql.sqltypes.AutoString(), nullable=True),
        sa.Column("passed", sa.Boolean(), nullable=False),
        sa.ForeignKeyConstraint(
            ["worker_id"],
            ["worker.id"],
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(
        op.f("ix_worker_compliance_check_worker_id"), "worker_compliance_check", ["worker_id"], unique=False
    )
    op.create_index(
        op.f("ix_worker_compliance_check_compare_worker_id"),
        "worker_compliance_check",
        ["compare_worker_id"],
        unique=False,
    )
    op.alter_column("chat", "user_id", existing_type=sa.VARCHAR(), nullable=False)
    op.create_index(op.f("ix_report_message_id"), "report", ["message_id"], unique=False)
    op.create_index(op.f("ix_vote_message_id"), "vote", ["message_id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_vote_message_id"), table_name="vote")
    op.drop_index(op.f("ix_report_message_id"), table_name="report")
    op.alter_column("chat", "user_id", existing_type=sa.VARCHAR(), nullable=True)
    op.drop_index(op.f("ix_worker_compliance_check_worker_id"), table_name="worker_compliance_check")
    op.drop_index(op.f("ix_worker_compliance_check_compare_worker_id"), table_name="worker_compliance_check")
    op.drop_table("worker_compliance_check")
    # ### end Alembic commands ###
