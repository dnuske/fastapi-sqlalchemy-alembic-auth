"""add wants_product_updates to user

Revision ID: b81e141faded
Revises: 49582bf94974
Create Date: 2022-07-24 14:23:25.203412

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b81e141faded'
down_revision = '49582bf94974'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('wants_product_updates', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'wants_product_updates')
    # ### end Alembic commands ###