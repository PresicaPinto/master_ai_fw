"""create chat_history table

Revision ID: a1b2c3d4e5f6
Revises: 1a2b3c4d5e6f
Create Date: 2025-09-25 10:00:00.000000

"""
from alembic import op
import sqlalchemy as sa
from datetime import datetime


# revision identifiers, used by Alembic.
revision = 'a1b2c3d4e5f6'
down_revision = '1a2b3c4d5e6f'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'chat_history',
        sa.Column('message_id', sa.String(length=36), nullable=False),
        sa.Column('user_message', sa.Text(), nullable=False),
        sa.Column('chatbot_response', sa.Text(), nullable=False),
        sa.Column('timestamp', sa.DateTime(), nullable=False, default=datetime.utcnow),
        sa.PrimaryKeyConstraint('message_id')
    )


def downgrade():
    op.drop_table('chat_history')
