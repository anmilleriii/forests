"""create_forests_table

Revision ID: 8a0a5e7eb101
Revises: 
Create Date: 2022-03-02 07:05:39.541834

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '8a0a5e7eb101'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('forests',
    sa.Column('uuid', postgresql.UUID(as_uuid=True), nullable=False),
    sa.Column('country', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('short_description', sa.String(), nullable=True),
    sa.Column('longitude', sa.Float(), nullable=True),
    sa.Column('latitude', sa.Float(), nullable=True),
    sa.Column('image_url', sa.String(), nullable=True),
    sa.Column('covered_area', sa.Integer(), nullable=True),
    sa.Column('carbon_stored', sa.Integer(), nullable=True),
    sa.Column('change_in_30_days', sa.Integer(), nullable=True),
    sa.Column('long_description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('forests')
    # ### end Alembic commands ###
