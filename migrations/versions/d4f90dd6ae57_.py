"""empty message

Revision ID: d4f90dd6ae57
Revises: 1e0dae60e4a2
Create Date: 2023-12-31 11:58:50.032700

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4f90dd6ae57'
down_revision = '1e0dae60e4a2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lesson', schema=None) as batch_op:
        batch_op.add_column(sa.Column('Lesson_Type', sa.String(length=50), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('lesson', schema=None) as batch_op:
        batch_op.drop_column('Lesson_Type')

    # ### end Alembic commands ###
