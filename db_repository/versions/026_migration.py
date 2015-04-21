from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
dnevnik = Table('dnevnik', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('ime_i_prezime', VARCHAR(length=50)),
    Column('razred', VARCHAR(length=4)),
    Column('ime', VARCHAR(length=15)),
    Column('prezime', VARCHAR(length=30)),
    Column('test', VARCHAR(length=30)),
)

dolaze = Table('dolaze', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('ime_i_prezime', VARCHAR(length=50)),
    Column('razred_id', INTEGER),
    Column('ime', VARCHAR(length=15)),
    Column('prezime', VARCHAR(length=30)),
)

razredi = Table('razredi', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('razred', VARCHAR(length=5)),
)

user = Table('user', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('nickname', VARCHAR(length=64)),
    Column('email', VARCHAR(length=120)),
    Column('about_me', VARCHAR(length=140)),
    Column('last_seen', TIMESTAMP),
    Column('username', VARCHAR(length=64)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['dnevnik'].drop()
    pre_meta.tables['dolaze'].drop()
    pre_meta.tables['razredi'].drop()
    pre_meta.tables['user'].columns['username'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['dnevnik'].create()
    pre_meta.tables['dolaze'].create()
    pre_meta.tables['razredi'].create()
    pre_meta.tables['user'].columns['username'].create()
