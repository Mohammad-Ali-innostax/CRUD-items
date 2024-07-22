"""migration 08

Revision ID: 3f3a2be81166
Revises: fcf7593c5ff7
Create Date: 2024-07-19 18:58:43.496744

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '3f3a2be81166'
down_revision: Union[str, None] = 'fcf7593c5ff7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('items', sa.Column('price', sa.Integer(), nullable=True))
    op.add_column('items', sa.Column('brand', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_items_brand'), 'items', ['brand'], unique=False)
    op.create_index(op.f('ix_items_price'), 'items', ['price'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_items_price'), table_name='items')
    op.drop_index(op.f('ix_items_brand'), table_name='items')
    op.drop_column('items', 'brand')
    op.drop_column('items', 'price')
    # ### end Alembic commands ###
