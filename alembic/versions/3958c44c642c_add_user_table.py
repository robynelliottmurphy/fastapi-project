"""add user table

Revision ID: 3958c44c642c
Revises: d58827017e98
Create Date: 2022-12-17 17:59:34.469164

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3958c44c642c'
down_revision = 'd58827017e98'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('users',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('created_at', sa.TIMESTAMP(timezone=True),
                              server_default=sa.text('now()'), nullable=False),
                    sa.PrimaryKeyConstraint('id'),
                    sa.UniqueConstraint('email')
                    )
    pass


def downgrade():
    op.drop_table('users')
    pass
