"""add content column to posts table

Revision ID: d58827017e98
Revises: 35afbbda6d7d
Create Date: 2022-12-16 12:06:51.558227

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd58827017e98'
down_revision = '35afbbda6d7d'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
