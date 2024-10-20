"""fix _chat

Revision ID: 1998c78129d6
Revises: 2f87752f7a70
Create Date: 2024-10-19 10:34:31.216985

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1998c78129d6'
down_revision = '2f87752f7a70'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.add_column(sa.Column('receiver_id', sa.UUID(), nullable=False))
        batch_op.alter_column('sender_id',
               existing_type=sa.UUID(),
               nullable=False)
        batch_op.create_foreign_key(None, 'user', ['receiver_id'], ['id'])
        batch_op.create_foreign_key(None, 'user', ['sender_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('chat', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('sender_id',
               existing_type=sa.UUID(),
               nullable=True)
        batch_op.drop_column('receiver_id')

    # ### end Alembic commands ###
