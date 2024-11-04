"""create post table

Revision ID: bd31461f7196
Revises: 
Create Date: 2024-11-02 23:56:18.085904

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd31461f7196'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table("post", sa.Column('id', sa.Integer(), nullable=False, primary_key=True),
                    sa.Column("title", sa.String(), nullable=False),
                    sa.Column("content", sa.String(), nullable=False))


def downgrade() -> None:
    op.drop_table("post")
    pass
    
