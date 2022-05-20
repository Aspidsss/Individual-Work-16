"""users

Revision ID: 127823405061
Revises: 
Create Date: 2022-05-21 01:15:42.625367

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '127823405061'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=64), nullable=True),
    sa.Column('lastname', sa.String(length=64), nullable=True),
    sa.Column('phone', sa.String(length=64), nullable=True),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('status', sa.Boolean(), nullable=True),
    sa.Column('password', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
