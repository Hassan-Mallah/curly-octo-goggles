"""create odds table

Revision ID: c2207da62c0d
Revises: 2f7394304c7a
Create Date: 2024-07-24 13:48:39.314358

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'c2207da62c0d'
down_revision: Union[str, None] = '2f7394304c7a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE TYPE type_choices AS ENUM ('win', 'lose', 'draw')")
    op.execute(
        """
        CREATE TABLE IF NOT EXISTS odds (
            id VARCHAR PRIMARY KEY,
            event_id VARCHAR REFERENCES events,
            type type_choices,
            value INTEGER,
            created_at TIMESTAMP WITHOUT TIME ZONE DEFAULT (now() at time zone 'utc')
        )
    """
    )


def downgrade() -> None:
    op.execute("DROP TABLE IF EXISTS odds")
    op.execute("DROP TYPE type_choices")
