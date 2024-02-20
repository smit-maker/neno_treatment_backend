"""Added appointment tables

Revision ID: ea1eb2b2b604
Revises: eb183e7606ab
Create Date: 2024-02-19 00:22:21.778090

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'ea1eb2b2b604'
down_revision: Union[str, None] = 'eb183e7606ab'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Appointments
    op.create_table('appointments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('user_id', sa.Integer(), nullable=True),
        sa.Column('sub_treatment_id', sa.Integer(), nullable=True),
        sa.Column('appointment_time', sa.DateTime(), nullable=True),
        sa.Column('status', sa.String(), nullable=True),
        sa.ForeignKeyConstraint(['sub_treatment_id'], ['sub_treatments.id'], ),
        sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_appointments_id'), 'appointments', ['id'], unique=False)


def downgrade() -> None:
    op.drop_index(op.f('ix_appointments_id'), table_name='appointments')
    op.drop_table('appointments')
