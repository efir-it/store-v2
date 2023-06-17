"""create db

Revision ID: 9130792668de
Revises: 
Create Date: 2023-06-17 17:53:19.155749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9130792668de'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('store', sa.Column('address', sa.String(length=300), nullable=False))
    op.add_column('store', sa.Column('separated', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('store', 'separated')
    op.drop_column('store', 'address')
    # ### end Alembic commands ###