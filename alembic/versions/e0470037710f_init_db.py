"""init_db

Revision ID: e0470037710f
Revises: 
Create Date: 2020-05-06 13:44:41.531920

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy import String
from sqlalchemy.dialects import postgresql
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = 'e0470037710f'
down_revision = None
branch_labels = None
depends_on = None


from alembic import context
from sqlalchemy.sql import table, column


def upgrade():
    schema_upgrades()
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_upgrades()


def downgrade():
    if context.get_x_argument(as_dictionary=True).get('data', None):
        data_downgrades()
    schema_downgrades()


def schema_upgrades():
    """schema upgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('format',
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('title')
    )
    op.create_table('level',
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('title')
    )
    op.create_table('role',
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('title')
    )
    op.create_table('status',
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('title')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('first_name', sa.String(length=50), nullable=True),
    sa.Column('last_name', sa.String(length=50), nullable=True),
    sa.Column('email', sqlalchemy_utils.types.email.EmailType(length=50), nullable=True),
    sa.Column('password', sqlalchemy_utils.types.password.PasswordType(), nullable=True),
    sa.Column('city', sa.String(), nullable=True),
    sa.Column('district', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=200), nullable=True),
    sa.Column('description', sa.String(length=1200), nullable=True),
    sa.Column('level_title', sa.String(), nullable=True),
    sa.Column('status_title', sa.String(), nullable=True),
    sa.Column('format_title', sa.String(), nullable=True),
    sa.Column('author_id', sa.Integer(), nullable=True),
    sa.Column('tags', postgresql.ARRAY(sa.String(length=50)), nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['format_title'], ['format.title'], ),
    sa.ForeignKeyConstraint(['level_title'], ['level.title'], ),
    sa.ForeignKeyConstraint(['status_title'], ['status.title'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('title')
    )
    op.create_table('project_type',
    sa.Column('title', sa.String(length=50), nullable=False),
    sa.Column('format_title', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['format_title'], ['format.title'], ),
    sa.PrimaryKeyConstraint('title')
    )
    op.create_table('user_roles',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('role_title', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['role_title'], ['role.title'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project_responsibility',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('responsible_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['responsible_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('project_types',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('project_id', sa.Integer(), nullable=True),
    sa.Column('project_type_title', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.ForeignKeyConstraint(['project_type_title'], ['project_type.title'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def schema_downgrades():
    """schema downgrade migrations go here."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project_types')
    op.drop_table('project_responsibility')
    op.drop_table('user_roles')
    op.drop_table('project_type')
    op.drop_table('project')
    op.drop_table('user')
    op.drop_table('status')
    op.drop_table('role')
    op.drop_table('level')
    op.drop_table('format')
    # ### end Alembic commands ###


def data_upgrades():
    """Add any optional data upgrade migrations here!"""

    format_table = table('format',
                         column('title', String),
                         )
    op.bulk_insert(format_table,
                   [{"title": "Digital"},
                    {"title": "Physical"}])
    level_table = table('level',
                        column('title', String),
                        )
    op.bulk_insert(level_table,
                   [{"title": "Base"},
                    {"title": "Standard"},
                    {"title": "Advanced"}])
    role_table = table('role',
                       column('title', String),
                       )
    op.bulk_insert(role_table,
                   [{"title": "Admin"},
                    {"title": "Teacher"},
                    {"title": "Methodologist"}])
    status_table = table('status',
                         column('title', String),
                         )
    op.bulk_insert(status_table,
                   [{"title": "Blueprint"},
                    {"title": "Proof of concept"},
                    {"title": "Ongoing project"},
                    {"title": "Finished"}])
    project_type_table = table('project_type',
                               column('title', String),
                               column('format_title', String),
                               )
    op.bulk_insert(project_type_table,
                   [{"title": "Presentation", "format_title": "Digital"},
                    {"title": "Audio", "format_title": "Digital"},
                    {"title": "Video", "format_title": "Digital"},
                    {"title": "Game (digital)", "format_title": "Digital"},
                    {"title": "Test", "format_title": "Digital"},
                    {"title": "Smart desk", "format_title": "Digital"},
                    {"title": "Other", "format_title": "Digital"},
                    {"title": "Schoolbook", "format_title": "Physical"},
                    {"title": "Book", "format_title": "Physical"},
                    {"title": "Teaching plan", "format_title": "Physical"},
                    {"title": "Game", "format_title": "Physical"},
                    {"title": "Printing", "format_title": "Physical"}])



def data_downgrades():
    """Add any optional data downgrade migrations here!"""
    pass