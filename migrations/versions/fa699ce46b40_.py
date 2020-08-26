"""empty message

Revision ID: fa699ce46b40
Revises: 4b647372dcb7
Create Date: 2020-08-24 15:57:51.689905

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fa699ce46b40'
down_revision = '4b647372dcb7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('address', sa.String(length=100), nullable=True))
    op.add_column('user', sa.Column('birthday', sa.DateTime(), nullable=True))
    op.add_column('user', sa.Column('head_url', sa.String(length=16), nullable=True))
    op.add_column('user', sa.Column('mail', sa.String(length=64), nullable=True))
    op.add_column('user', sa.Column('sex', sa.Enum('男', '女', '保密'), nullable=True))
    op.add_column('user', sa.Column('tel', sa.String(length=11), nullable=True))
    op.create_unique_constraint(None, 'user', ['tel'])
    op.create_unique_constraint(None, 'user', ['mail'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_constraint(None, 'user', type_='unique')
    op.drop_column('user', 'tel')
    op.drop_column('user', 'sex')
    op.drop_column('user', 'mail')
    op.drop_column('user', 'head_url')
    op.drop_column('user', 'birthday')
    op.drop_column('user', 'address')
    # ### end Alembic commands ###
