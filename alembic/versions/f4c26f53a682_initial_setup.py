"""Initial setup

Revision ID: f4c26f53a682
Revises: 
Create Date: 2022-05-19 23:11:43.030081

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f4c26f53a682'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "users",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("nickname", sa.String),
    )

    op.create_table(
        "tracks",
        sa.Column("id", sa.Integer, primary_key=True),
        sa.Column("title", sa.String),
    )


def downgrade():
    op.drop_table("users")
    op.drop_table("tracks")

