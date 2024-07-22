"""migration 02

Revision ID: fbc17963132f
Revises: 71f92ed530f8
Create Date: 2024-07-19 18:09:44.536510

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fbc17963132f'
down_revision: Union[str, None] = '71f92ed530f8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
