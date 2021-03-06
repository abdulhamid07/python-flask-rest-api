"""add constraint foreign key

Revision ID: 77b435a042a5
Revises: 49fa57b389d0
Create Date: 2021-09-25 20:25:29.868977

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77b435a042a5'
down_revision = '49fa57b389d0'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key(None, 'mahasiswa', 'dosen', ['dosen_satu'], ['id'], ondelete='SET NULL')
    op.create_foreign_key(None, 'mahasiswa', 'dosen', ['dosen_dua'], ['id'], ondelete='SET NULL')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'mahasiswa', type_='foreignkey')
    op.drop_constraint(None, 'mahasiswa', type_='foreignkey')
    # ### end Alembic commands ###
