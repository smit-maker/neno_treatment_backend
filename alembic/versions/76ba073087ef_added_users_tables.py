"""Added Users tables

Revision ID: 76ba073087ef
Revises: 
Create Date: 2024-02-18 11:38:07.675649

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '76ba073087ef'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Branches 
    op.create_table('branches',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_branches_id'), 'branches', ['id'], unique=False)
    op.create_index(op.f('ix_branches_name'), 'branches', ['name'], unique=True)
    
    # Users 
    op.create_table('users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('username', sa.String(), nullable=True),
        sa.Column('email', sa.String(), nullable=True),
        sa.Column('f_name', sa.String(), nullable=True),
        sa.Column('l_name', sa.String(), nullable=True),
        sa.Column('password', sa.String(), nullable=True),
        sa.Column('gender', sa.String(), nullable=True),
        sa.Column('dob', sa.DateTime(), nullable=True),
        sa.Column('profile_picture', sa.String(), nullable=True),
        sa.Column('disabled', sa.Boolean(), nullable=True),
        sa.Column('branch_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['branch_id'], ['branches.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=False)
    op.create_index(op.f('ix_users_password'), 'users', ['password'], unique=False)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)

def downgrade() -> None:
    # Users
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_password'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_table('users')

    # Branches 
    op.drop_index(op.f('ix_branches_name'), table_name='branches')
    op.drop_index(op.f('ix_branches_id'), table_name='branches')
    op.drop_table('branches')
