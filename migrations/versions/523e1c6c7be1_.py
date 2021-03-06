"""empty message

Revision ID: 523e1c6c7be1
Revises: fe0e5b464ac2
Create Date: 2017-06-25 10:32:23.660945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '523e1c6c7be1'
down_revision = 'fe0e5b464ac2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('session',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=60), nullable=True),
    sa.Column('description', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('session')
    # ### end Alembic commands ###
