"""fix_migrations_user_password

Revision ID: 470b4c31870f
Revises: 78d94810cfbe
Create Date: 2025-01-22 16:42:56.662598

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '470b4c31870f'
down_revision: Union[str, None] = '78d94810cfbe'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'username',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.String(length=60),
               existing_nullable=False)
    op.alter_column('user', 'password',
               existing_type=sa.VARCHAR(length=30),
               type_=sa.String(length=60),
               existing_nullable=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('user', 'password',
               existing_type=sa.String(length=60),
               type_=sa.VARCHAR(length=30),
               existing_nullable=False)
    op.alter_column('user', 'username',
               existing_type=sa.String(length=60),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)
    # ### end Alembic commands ###
