"""add Department

Revision ID: 2442669564cc
Revises: 2f0719311303
Create Date: 2024-06-29 17:32:19.361273

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2442669564cc'
down_revision = '2f0719311303'
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
