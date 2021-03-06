"""empty message

Revision ID: 03b47f869334
Revises: c6e5fbbfb13b
Create Date: 2022-03-10 10:03:35.710905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '03b47f869334'
down_revision = 'c6e5fbbfb13b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('question', sa.Column('isDelete', sa.Integer(), nullable=True))
    op.add_column('user', sa.Column('update_time', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'update_time')
    op.drop_column('question', 'isDelete')
    # ### end Alembic commands ###
