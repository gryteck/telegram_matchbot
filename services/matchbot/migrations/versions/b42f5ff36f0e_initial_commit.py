"""Initial commit

Revision ID: b42f5ff36f0e
Revises: 
Create Date: 2024-05-23 16:28:29.341370

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = 'b42f5ff36f0e'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('promocodes')
    op.drop_table('visits')
    op.drop_index('qr_id_idx', table_name='qrcodes')
    op.drop_table('qrcodes')
    op.drop_index('user_id_idx', table_name='users')
    op.create_index(op.f('ix_users_user_id'), 'users', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_users_user_id'), table_name='users')
    op.create_index('user_id_idx', 'users', ['id'], unique=False)
    op.create_table('quiz_questions',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('question', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('answer', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('created_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='quiz_questions_pkey')
    )
    op.create_index('ix_quiz_questions_id', 'quiz_questions', ['id'], unique=False)
    op.create_table('qrcodes',
    sa.Column('qr_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('username', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('age', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('gender', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('join_date', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("timezone('Europe/Moscow'::text, now())"), autoincrement=False, nullable=False),
    sa.Column('active_date', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("timezone('Europe/Moscow'::text, now())"), autoincrement=False, nullable=False),
    sa.Column('visit_count', sa.SMALLINT(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('status', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('promocode', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('qr_id', name='qrcodes_pkey'),
    sa.UniqueConstraint('id', name='qrcodes_id_key')
    )
    op.create_index('qr_id_idx', 'qrcodes', ['qr_id'], unique=False)
    op.create_table('visits',
    sa.Column('visit_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('date', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("timezone('Europe/Moscow'::text, now())"), autoincrement=False, nullable=False),
    sa.Column('id', sa.BIGINT(), autoincrement=False, nullable=False),
    sa.Column('username', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('age', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('gender', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('visit_count', sa.SMALLINT(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('status', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('promocode', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('visit_id', name='visits_pkey')
    )
    op.create_table('promocodes',
    sa.Column('promocode_id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('join_date', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("timezone('Europe/Moscow'::text, now())"), autoincrement=False, nullable=False),
    sa.Column('active_date', postgresql.TIMESTAMP(timezone=True), server_default=sa.text("timezone('Europe/Moscow'::text, now())"), autoincrement=False, nullable=False),
    sa.Column('visit_count', sa.SMALLINT(), server_default=sa.text('0'), autoincrement=False, nullable=False),
    sa.Column('promocode', sa.TEXT(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('promocode_id', name='promocodes_pkey')
    )
    # ### end Alembic commands ###