"""empty message

Revision ID: 841694e3d6e9
Revises: 
Create Date: 2021-03-28 10:40:02.212064

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '841694e3d6e9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('mailing_list')
    op.drop_table('event')
    op.drop_table('user')
    op.drop_table('meeting')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('meeting',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('host', sa.VARCHAR(length=25), nullable=False),
    sa.Column('date', sa.DATETIME(), nullable=False),
    sa.Column('dateText', sa.VARCHAR(length=25), nullable=False),
    sa.Column('timeText', sa.VARCHAR(length=25), nullable=False),
    sa.Column('time', sa.TIME(), nullable=False),
    sa.Column('link', sa.VARCHAR(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=20), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), nullable=False),
    sa.Column('imageFile', sa.VARCHAR(length=20), nullable=False),
    sa.Column('password', sa.VARCHAR(length=60), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('event',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('title', sa.VARCHAR(length=75), nullable=False),
    sa.Column('location', sa.VARCHAR(length=25), nullable=False),
    sa.Column('timeText', sa.VARCHAR(length=25), nullable=False),
    sa.Column('dateText', sa.VARCHAR(length=25), nullable=False),
    sa.Column('date', sa.DATETIME(), nullable=False),
    sa.Column('time', sa.TIME(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('mailing_list',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('email', sa.VARCHAR(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
