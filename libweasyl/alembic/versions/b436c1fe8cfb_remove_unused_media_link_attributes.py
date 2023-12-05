"""Remove unused media link attributes

Revision ID: b436c1fe8cfb
Revises: 3f18ecfaf637
Create Date: 2017-06-10 04:08:47.861911

"""

# revision identifiers, used by Alembic.
revision = 'b436c1fe8cfb'
down_revision = '3f18ecfaf637'

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('media_media_links', 'attributes')
    op.drop_column('submission_media_links', 'attributes')
    op.drop_column('user_media_links', 'attributes')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_media_links', sa.Column('attributes', postgresql.HSTORE(), server_default=sa.text(u"''::hstore"), autoincrement=False, nullable=False))
    op.add_column('submission_media_links', sa.Column('attributes', postgresql.HSTORE(), server_default=sa.text(u"''::hstore"), autoincrement=False, nullable=False))
    op.add_column('media_media_links', sa.Column('attributes', postgresql.HSTORE(), server_default=sa.text(u"''::hstore"), autoincrement=False, nullable=False))
    # ### end Alembic commands ###