"""create table user

Revision ID: 276126c72b42
Revises: 
Create Date: 2021-09-25 01:41:13.357638

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '276126c72b42'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.BigInteger(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('email', sa.String(length=60), nullable=False),
    sa.Column('password', sa.String(length=250), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
