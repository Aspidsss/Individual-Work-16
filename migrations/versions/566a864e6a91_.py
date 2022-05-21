"""empty message

Revision ID: 566a864e6a91
Revises: 3f3561848983
Create Date: 2022-05-21 13:26:49.728714

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '566a864e6a91'
down_revision = '3f3561848983'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('login', sa.String(length=64), nullable=True))
    op.drop_column('user', 'firstname')
    op.drop_column('user', 'status')
    op.drop_column('user', 'email')
    op.drop_column('user', 'phone')
    op.drop_column('user', 'lastname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('lastname', sa.VARCHAR(length=64), nullable=True))
    op.add_column('user', sa.Column('phone', sa.VARCHAR(length=64), nullable=True))
    op.add_column('user', sa.Column('email', sa.VARCHAR(length=64), nullable=True))
    op.add_column('user', sa.Column('status', sa.BOOLEAN(), nullable=True))
    op.add_column('user', sa.Column('firstname', sa.VARCHAR(length=64), nullable=True))
    op.drop_column('user', 'login')
    # ### end Alembic commands ###
