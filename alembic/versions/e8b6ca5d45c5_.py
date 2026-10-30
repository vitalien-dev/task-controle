"""empty message

Revision ID: e8b6ca5d45c5
Revises: d8fc56d0cb64
Create Date: 2026-10-30 13:52:45.183878

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'e8b6ca5d45c5'
down_revision: Union[str, Sequence[str], None] = 'd8fc56d0cb64'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    pass


def downgrade() -> None:
    """Downgrade schema."""
    pass
