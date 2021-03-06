"""remove api_key

Revision ID: 5d166a1e5ad9
Revises: 6c0e9c6a04ad
Create Date: 2021-10-14 20:08:55.696648

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5d166a1e5ad9'
down_revision = '6c0e9c6a04ad'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'api_key')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('api_key', sa.VARCHAR(length=511), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
