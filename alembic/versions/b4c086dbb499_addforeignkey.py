"""addforeignkey

Revision ID: b4c086dbb499
Revises: b20ebd41fd23
Create Date: 2024-11-04 03:49:57.337075

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b4c086dbb499'
down_revision: Union[str, None] = 'b20ebd41fd23'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('post', sa.Column('user_id', sa.Integer(), nullable=False))
    op.create_foreign_key('post_user_fk', source_table='post', referent_table='users',
                          local_cols=['user_id'] , remote_cols=['id'], ondelete="CASCADE")
    pass


def downgrade() -> None:
    op.drop_constraint('post_user_fk', table_name='post')
    op.drop_column('post','user_id')
    pass
