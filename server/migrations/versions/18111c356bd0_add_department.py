"""add Department

Revision ID: 18111c356bd0
Revises: 6850be696c97
Create Date: 2025-03-26 16:39:13.117128

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18111c356bd0'
down_revision = '6850be696c97'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
