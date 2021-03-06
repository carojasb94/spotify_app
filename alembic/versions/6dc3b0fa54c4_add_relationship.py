"""add relationship

Revision ID: 6dc3b0fa54c4
Revises: f4c26f53a682
Create Date: 2022-05-20 00:39:43.767672

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6dc3b0fa54c4'
down_revision = 'f4c26f53a682'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_tracks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('track_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['track_id'], ['tracks.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('tracks', sa.Column('title', sa.String(), nullable=True))
    op.add_column('tracks', sa.Column('artist', sa.String(), nullable=True))
    op.add_column('tracks', sa.Column('album', sa.String(), nullable=True))
    op.add_column('tracks', sa.Column('timestamp', sa.DateTime(), nullable=True))
    op.add_column('tracks', sa.Column('played_at', sa.Date(), nullable=True))
    op.add_column('tracks', sa.Column('inserted_at', sa.DateTime(), nullable=True))
    op.drop_column('tracks', 'nickname')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tracks', sa.Column('nickname', sa.VARCHAR(), nullable=True))
    op.drop_column('tracks', 'inserted_at')
    op.drop_column('tracks', 'played_at')
    op.drop_column('tracks', 'timestamp')
    op.drop_column('tracks', 'album')
    op.drop_column('tracks', 'artist')
    op.drop_column('tracks', 'title')
    op.drop_table('user_tracks')
    # ### end Alembic commands ###
