"""create posts table

Revision ID: bf53dafa8249
Revises: 
Create Date: 2022-01-03 20:00:59.336161

"""
from alembic import op
import sqlalchemy as sa



# revision identifiers, used by Alembic.
revision = 'bf53dafa8249'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
