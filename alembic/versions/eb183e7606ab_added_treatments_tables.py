"""Added Treatments tables

Revision ID: eb183e7606ab
Revises: 76ba073087ef
Create Date: 2024-02-18 11:38:55.116562

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'eb183e7606ab'
down_revision: Union[str, None] = '76ba073087ef'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Treatments
    op.create_table('treatments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('treatments_picture', sa.String(), nullable=True),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_treatments_id'), 'treatments', ['id'], unique=False)
    op.create_index(op.f('ix_treatments_name'), 'treatments', ['name'], unique=True)
    
    # Sub Treatments
    op.create_table('sub_treatments',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('name', sa.String(), nullable=True),
        sa.Column('treatments_picture', sa.String(), nullable=True),
        sa.Column('price', sa.Float(), nullable=True),
        sa.Column('mrp', sa.Float(), nullable=True),
        sa.Column('discount', sa.Float(), nullable=True),
        sa.Column('description', sa.String(), nullable=True),
        sa.Column('treatment_time', sa.String(), nullable=True),
        sa.Column('treatment_id', sa.Integer(), nullable=True),
        sa.ForeignKeyConstraint(['treatment_id'], ['treatments.id'], ),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_sub_treatments_id'), 'sub_treatments', ['id'], unique=False)
    op.create_index(op.f('ix_sub_treatments_name'), 'sub_treatments', ['name'], unique=True)
   
def downgrade() -> None:
    #  Sub Treatments
    op.drop_index(op.f('ix_sub_treatments_name'), table_name='sub_treatments')
    op.drop_index(op.f('ix_sub_treatments_id'), table_name='sub_treatments')
    op.drop_table('sub_treatments')
    
    # Treatments
    op.drop_index(op.f('ix_treatments_name'), table_name='treatments')
    op.drop_index(op.f('ix_treatments_id'), table_name='treatments')
    op.drop_table('treatments')
