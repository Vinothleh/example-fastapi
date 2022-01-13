"""add content column to posts table

Revision ID: 028c727bcbbd
Revises: bf53dafa8249
Create Date: 2022-01-13 08:40:53.886749

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '028c727bcbbd'
down_revision = 'bf53dafa8249'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String, nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
