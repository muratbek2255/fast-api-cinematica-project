"""Added movie and rent model

Revision ID: d1f252b85996
Revises: cfd833170123
Create Date: 2023-05-02 18:11:39.001921

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1f252b85996'
down_revision = 'cfd833170123'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('row', sa.String(length=125), nullable=False),
    sa.Column('place', sa.String(length=125), nullable=False),
    sa.Column('is_rent', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('basemodels')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('basemodels',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='basemodels_pkey')
    )
    op.drop_table('rents')
    # ### end Alembic commands ###
