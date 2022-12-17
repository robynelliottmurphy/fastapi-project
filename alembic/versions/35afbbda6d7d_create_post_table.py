"""create post table

Revision ID: 35afbbda6d7d
Revises: 
Create Date: 2022-12-16 11:54:02.586588

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '35afbbda6d7d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
