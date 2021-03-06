"""followers

Revision ID: 11ab9d27c012
Revises: 2e4eac215cff
Create Date: 2020-06-06 12:19:29.391682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11ab9d27c012'
down_revision = '2e4eac215cff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
