"""Initial Commit

Revision ID: a645a3e2b265
Revises: 
Create Date: 2019-04-15 23:24:06.225006

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a645a3e2b265'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('models',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_models'))
    )
    op.create_index('my_index', 'models', ['name'], unique=True, mysql_length=255)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('my_index', table_name='models')
    op.drop_table('models')
    # ### end Alembic commands ###
