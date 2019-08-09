"""empty message

Revision ID: 246b5b6123af
Revises: 9d5753192ac9
Create Date: 2019-08-09 19:41:03.995654

"""

from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils


# revision identifiers, used by Alembic.
revision = '246b5b6123af'
down_revision = '9d5753192ac9'


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('settings', sa.Column('paytm_live_merchant', sa.String(), nullable=True))
    op.add_column('settings', sa.Column('paytm_live_secret', sa.String(), nullable=True))
    op.add_column('settings', sa.Column('paytm_mode', sa.String(), nullable=True))
    op.add_column('settings', sa.Column('paytm_sandbox_merchant', sa.String(), nullable=True))
    op.add_column('settings', sa.Column('paytm_sandbox_secret', sa.String(), nullable=True))
    op.add_column('settings', sa.Column('is_paytm_activated', sa.Boolean(), server_default='False', nullable=False))
    # ### end Alembic commands ###


def downgrade():
    op.drop_column('settings', 'paytm_sandbox_secret')
    op.drop_column('settings', 'paytm_sandbox_merchant')
    op.drop_column('settings', 'paytm_mode')
    op.drop_column('settings', 'paytm_live_secret')
    op.drop_column('settings', 'paytm_live_merchant')
    op.drop_column('settings', 'is_paytm_activated')
    # ### end Alembic commands ###
