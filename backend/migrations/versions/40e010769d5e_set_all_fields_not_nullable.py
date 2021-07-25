"""Set all fields not nullable

Revision ID: 40e010769d5e
Revises: 60e166b075a1
Create Date: 2021-07-26 00:22:17.467616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '40e010769d5e'
down_revision = '60e166b075a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('auth_keys', 'auth_key_id',
               existing_type=sa.BIGINT(),
               nullable=False)
    op.alter_column('auth_keys', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('tasks', 'todo_list_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('tasks', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('tasks', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=False)
    op.alter_column('todo_lists', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('todo_lists', 'title',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'nickname',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'password',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('users', 'nickname',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('todo_lists', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('todo_lists', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('tasks', 'completed',
               existing_type=sa.BOOLEAN(),
               nullable=True)
    op.alter_column('tasks', 'title',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('tasks', 'todo_list_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('auth_keys', 'user_id',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('auth_keys', 'auth_key_id',
               existing_type=sa.BIGINT(),
               nullable=True)
    # ### end Alembic commands ###