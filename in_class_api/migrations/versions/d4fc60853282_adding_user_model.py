"""Adding User Model

Revision ID: d4fc60853282
Revises: 5ff1be27cd00
Create Date: 2020-11-05 10:32:41.993220

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4fc60853282'
down_revision = '5ff1be27cd00'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(length=200), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('email', sa.String(length=150), nullable=True),
    sa.Column('password', sa.String(length=256), nullable=False),
    sa.Column('token', sa.String(length=400), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.Column('token_refreshed', sa.Boolean(), nullable=True),
    sa.Column('date_refreshed', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user')
    # ### end Alembic commands ###
