"""empty message

Revision ID: 0a0a183fee0f
Revises: 
Create Date: 2019-08-25 20:35:02.974748

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0a0a183fee0f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredient',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('size',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=80), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('order',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('client_name', sa.String(length=80), nullable=True),
    sa.Column('client_dni', sa.String(length=10), nullable=True),
    sa.Column('client_address', sa.String(length=128), nullable=True),
    sa.Column('client_phone', sa.String(length=15), nullable=True),
    sa.Column('date', sa.DateTime(), nullable=True),
    sa.Column('size_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['size_id'], ['size._id'], ),
    sa.PrimaryKeyConstraint('_id')
    )
    op.create_table('order_detail',
    sa.Column('_id', sa.Integer(), nullable=False),
    sa.Column('ingredient_price', sa.Float(), nullable=True),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('ingredient_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_id'], ['ingredient._id'], ),
    sa.ForeignKeyConstraint(['order_id'], ['order._id'], ),
    sa.PrimaryKeyConstraint('_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order_detail')
    op.drop_table('order')
    op.drop_table('size')
    op.drop_table('ingredient')
    # ### end Alembic commands ###
