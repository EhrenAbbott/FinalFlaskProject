"""empty message

Revision ID: 0d0717decb76
Revises: 
Create Date: 2023-05-26 12:51:30.107533

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0d0717decb76'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('first_name', sa.String(length=150), nullable=True),
    sa.Column('last_name', sa.String(length=150), nullable=True),
    sa.Column('email', sa.String(length=150), nullable=False),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('g_auth_verify', sa.Boolean(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('token')
    )
    op.create_table('dict',
    sa.Column('id', sa.String(), nullable=False),
    sa.Column('word', sa.String(length=50), nullable=True),
    sa.Column('meaning', sa.String(length=300), nullable=True),
    sa.Column('part_of_speech', sa.String(length=10), nullable=True),
    sa.Column('gender', sa.String(length=10), nullable=True),
    sa.Column('plural', sa.String(length=50), nullable=True),
    sa.Column('present_tense', sa.String(length=30), nullable=True),
    sa.Column('past_tense', sa.String(length=30), nullable=True),
    sa.Column('past_part', sa.String(length=30), nullable=True),
    sa.Column('perfect_aux', sa.String(length=10), nullable=True),
    sa.Column('preposition', sa.String(length=20), nullable=True),
    sa.Column('case_triggered', sa.String(length=15), nullable=True),
    sa.Column('user_token', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['user_token'], ['user.token'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('dict')
    op.drop_table('user')
    # ### end Alembic commands ###