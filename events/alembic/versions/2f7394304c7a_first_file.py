"""create events table

Revision ID: 2f7394304c7a
Revises: 
Create Date: 2024-07-23 11:18:18.930226

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = '2f7394304c7a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(
        """
        CREATE TABLE IF NOT EXISTS events (
            id SERIAL PRIMARY KEY,
            name VARCHAR,
            created_at TIMESTAMP,
            location VARCHAR,
            teams VARCHAR []
        )
    """
    )



def downgrade() -> None:
    op.execute(
        """
        DROP TABLE IF EXISTS events
    """
    )
