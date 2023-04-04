"""Change enum value to full name

Revision ID: 502a018c8d3b
Revises: 30c5ced21b9a
Create Date: 2023-04-04 16:56:58.842476

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '502a018c8d3b'
down_revision = '30c5ced21b9a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fractal', schema=None) as batch_op:
        batch_op.alter_column('fractal_type',
               existing_type=sa.VARCHAR(length=6),
               type_=sa.Enum('mandelbrot', 'julia', name='myenum'),
               existing_nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('fractal', schema=None) as batch_op:
        batch_op.alter_column('fractal_type',
               existing_type=sa.Enum('mandelbrot', 'julia', name='myenum'),
               type_=sa.VARCHAR(length=6),
               existing_nullable=True)

    # ### end Alembic commands ###
