"""fix type devices

Revision ID: d0810b5ae8d8
Revises: 6ce55d48d094
Create Date: 2023-06-16 12:26:26.405337

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0810b5ae8d8'
down_revision = '6ce55d48d094'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('drivers_type_device_id_fkey', 'drivers', type_='foreignkey')
    op.drop_column('drivers', 'type_device_id')
    op.create_unique_constraint(None, 'type_device', ['name'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'type_device', type_='unique')
    op.add_column('drivers', sa.Column('type_device_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key('drivers_type_device_id_fkey', 'drivers', 'type_device', ['type_device_id'], ['id'])
    # ### end Alembic commands ###
