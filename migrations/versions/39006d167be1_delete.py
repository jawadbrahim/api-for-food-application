"""delete

Revision ID: 39006d167be1
Revises: 392530f48815
Create Date: 2024-07-17 17:51:21.226978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '39006d167be1'
down_revision = '392530f48815'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('foods', schema=None) as batch_op:
        batch_op.drop_column('status')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('foods', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=True))

    # ### end Alembic commands ###