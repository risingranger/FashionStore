"""empty message

Revision ID: 4215e77b942b
Revises: 8cda5671f176
Create Date: 2017-11-20 16:43:39.381080

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4215e77b942b'
down_revision = '8cda5671f176'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reference', sa.String(length=5), nullable=True),
    sa.Column('first_name', sa.String(length=20), nullable=True),
    sa.Column('last_name', sa.String(length=20), nullable=True),
    sa.Column('phone_number', sa.Integer(), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('address', sa.String(length=100), nullable=True),
    sa.Column('city', sa.String(length=100), nullable=True),
    sa.Column('state', sa.String(length=20), nullable=True),
    sa.Column('country', sa.String(length=20), nullable=True),
    sa.Column('status', sa.String(length=10), nullable=True),
    sa.Column('payment_type', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('order__item',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_id', sa.Integer(), nullable=True),
    sa.Column('product_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['order_id'], ['order.id'], ),
    sa.ForeignKeyConstraint(['product_id'], ['product.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order__item')
    op.drop_table('order')
    # ### end Alembic commands ###