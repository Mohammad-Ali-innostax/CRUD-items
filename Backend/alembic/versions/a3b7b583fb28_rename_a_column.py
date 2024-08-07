"""rename a column

Revision ID: a3b7b583fb28
Revises: a4d63b2c91e1
Create Date: 2024-07-24 14:38:12.026811

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a3b7b583fb28'
down_revision: Union[str, None] = 'a4d63b2c91e1'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    
    op.drop_index('ix_AuthenticationTable_Username', table_name='AuthenticationTable')
    op.drop_column('AuthenticationTable', 'Username')
    
    op.add_column('AuthenticationTable', sa.Column('username', sa.String(), nullable=True))
    op.create_index(op.f('ix_AuthenticationTable_username'), 'AuthenticationTable', ['username'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('AuthenticationTable', sa.Column('Username', sa.VARCHAR(), nullable=True))
    op.drop_index(op.f('ix_AuthenticationTable_username'), table_name='AuthenticationTable')
    op.create_index('ix_AuthenticationTable_Username', 'AuthenticationTable', ['Username'], unique=False)
    op.drop_column('AuthenticationTable', 'username')
    # ### end Alembic commands ###
