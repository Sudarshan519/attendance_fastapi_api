"""attendance table upgrade

Revision ID: cffd83bbfe76
Revises: 
Create Date: 2023-07-06 09:13:51.920087

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'cffd83bbfe76'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('uq_company_employee', 'employeemodel', type_='unique')
    op.create_table('book',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('rating', mysql.FLOAT(), nullable=True),
    sa.Column('time_created', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('time_updated', mysql.DATETIME(), nullable=True),
    sa.Column('author_id', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], name='book_ibfk_1'),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.create_index('ix_book_id', 'book', ['id'], unique=False)
    op.create_table('author',
    sa.Column('id', mysql.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', mysql.VARCHAR(length=256), nullable=True),
    sa.Column('age', mysql.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('time_created', mysql.DATETIME(), server_default=sa.text('CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('time_updated', mysql.DATETIME(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###
