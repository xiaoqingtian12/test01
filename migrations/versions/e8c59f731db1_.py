"""empty message

Revision ID: e8c59f731db1
Revises: 398f9c1a0b6e
Create Date: 2022-03-03 14:59:21.143468

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e8c59f731db1'
down_revision = '398f9c1a0b6e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('age', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('sex', sa.String(length=2), nullable=False))
    op.add_column('user', sa.Column('mobile', sa.Integer(), nullable=False))
    op.add_column('user', sa.Column('address', sa.String(length=50), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'address')
    op.drop_column('user', 'mobile')
    op.drop_column('user', 'sex')
    op.drop_column('user', 'age')
    # ### end Alembic commands ###
