from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
dolaze = Table('dolaze', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('ime_i_prezime', String(length=50)),
    Column('prezime', String(length=30)),
    Column('ime', String(length=15)),
    Column('razred_id', Integer),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['dolaze'].columns['ime'].create()
    post_meta.tables['dolaze'].columns['prezime'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['dolaze'].columns['ime'].drop()
    post_meta.tables['dolaze'].columns['prezime'].drop()
