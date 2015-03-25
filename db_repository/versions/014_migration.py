from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
djaci = Table('djaci', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('prezime', VARCHAR(length=30)),
    Column('ime', VARCHAR(length=15)),
    Column('razred_id', INTEGER),
    Column('email', VARCHAR(length=120)),
    Column('nadimak', VARCHAR(length=15)),
)

razredi = Table('razredi', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('oznaka', VARCHAR(length=5)),
    Column('razrednica', VARCHAR(length=30)),
)

razredi = Table('razredi', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('razred', String(length=5)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['djaci'].drop()
    pre_meta.tables['razredi'].columns['oznaka'].drop()
    pre_meta.tables['razredi'].columns['razrednica'].drop()
    post_meta.tables['razredi'].columns['razred'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['djaci'].create()
    pre_meta.tables['razredi'].columns['oznaka'].create()
    pre_meta.tables['razredi'].columns['razrednica'].create()
    post_meta.tables['razredi'].columns['razred'].drop()
