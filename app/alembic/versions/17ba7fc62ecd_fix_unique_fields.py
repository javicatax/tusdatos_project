"""fix_unique_fields

Revision ID: 17ba7fc62ecd
Revises: ec707baf8690
Create Date: 2025-01-22 19:47:47.244442

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '17ba7fc62ecd'
down_revision: Union[str, None] = 'ec707baf8690'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_attendee_nombre'), 'attendee', ['nombre'], unique=True)
    op.drop_index('ix_event_name', table_name='event')
    op.create_index(op.f('ix_event_name'), 'event', ['name'], unique=True)
    op.create_index(op.f('ix_sessionevent_nombre'), 'sessionevent', ['nombre'], unique=True)
    op.create_index(op.f('ix_speaker_nombre'), 'speaker', ['nombre'], unique=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_speaker_nombre'), table_name='speaker')
    op.drop_index(op.f('ix_sessionevent_nombre'), table_name='sessionevent')
    op.drop_index(op.f('ix_event_name'), table_name='event')
    op.create_index('ix_event_name', 'event', ['name'], unique=False)
    op.drop_index(op.f('ix_attendee_nombre'), table_name='attendee')
    # ### end Alembic commands ###
