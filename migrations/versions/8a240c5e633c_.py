""".

Revision ID: 8a240c5e633c
Revises: 0d2489efd8e3
Create Date: 2019-11-25 14:01:54.572796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8a240c5e633c'
down_revision = '0d2489efd8e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('friends',
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('friend_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['friend_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], )
    )
    op.drop_table('followers')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.INTEGER(), nullable=True),
    sa.Column('followed_id', sa.INTEGER(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    op.drop_table('friends')
    # ### end Alembic commands ###
