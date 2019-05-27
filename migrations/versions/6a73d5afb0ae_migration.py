"""Migration

Revision ID: 6a73d5afb0ae
Revises: fba55687c999
Create Date: 2019-05-27 11:27:05.392468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6a73d5afb0ae'
down_revision = 'fba55687c999'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('comment_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'posts', 'comments', ['comment_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'posts', type_='foreignkey')
    op.drop_column('posts', 'comment_id')
    # ### end Alembic commands ###
