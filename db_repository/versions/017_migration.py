from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
iz_dnevnika = Table('iz_dnevnika', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('ime_i_prezime', String(length=50)),
    Column('razred', String(length=4)),
    Column('ime', String(length=15)),
    Column('prezime', String(length=30)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['iz_dnevnika'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['iz_dnevnika'].drop()
