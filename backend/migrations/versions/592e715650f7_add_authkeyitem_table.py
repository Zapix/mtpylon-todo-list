"""Add AuthKeyItem table

Revision ID: 592e715650f7
Revises: 3f3d1394abc5
Create Date: 2021-09-12 18:31:38.825165

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '592e715650f7'
down_revision = '3f3d1394abc5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_key_items',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('auth_key_id', sa.BigInteger(), nullable=False),
    sa.Column('auth_key', sa.LargeBinary(length=2048), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('auth_key_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('auth_key_items')
    # ### end Alembic commands ###
