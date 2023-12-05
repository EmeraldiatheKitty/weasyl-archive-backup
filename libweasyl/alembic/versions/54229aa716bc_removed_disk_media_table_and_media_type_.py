"""Removed disk_media table, and media_type column from media table

Revision ID: 54229aa716bc
Revises: 39f2ff4b7fa6
Create Date: 2020-01-26 17:43:45.548000

"""

# revision identifiers, used by Alembic.
revision = '54229aa716bc'
down_revision = 'a1dac55f8355'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('disk_media')
    op.drop_column('media', 'media_type')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('media', sa.Column('media_type', sa.VARCHAR(length=32), autoincrement=False, nullable=False))
    op.create_table('disk_media',
    sa.Column('mediaid', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('file_path', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('file_url', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['mediaid'], [u'media.mediaid'], name=u'disk_media_mediaid_fkey', onupdate=u'CASCADE', ondelete=u'CASCADE'),
    sa.PrimaryKeyConstraint('mediaid', name=u'disk_media_pkey')
    )
    # ### end Alembic commands ###