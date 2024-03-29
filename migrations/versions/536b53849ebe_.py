"""empty message

Revision ID: 536b53849ebe
Revises: 9ae3d1e7960b
Create Date: 2024-02-17 12:27:48.469006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '536b53849ebe'
down_revision = '9ae3d1e7960b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lesson', schema=None) as batch_op:
        batch_op.add_column(sa.Column('lessonTime', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lesson', schema=None) as batch_op:
        batch_op.drop_column('lessonTime')

    # ### end Alembic commands ###
