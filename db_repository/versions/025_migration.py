from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
iz_dnevnika_acc = Table('iz_dnevnika_acc', pre_meta,
    Column('ime_i_prezime', VARCHAR(length=150)),
    Column('razred', VARCHAR(length=4)),
    Column('ime', VARCHAR(length=15)),
    Column('prezime', VARCHAR(length=40)),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('nickname', String(length=64)),
    Column('username', String(length=64)),
    Column('email', String(length=120)),
    Column('about_me', String(length=140)),
    Column('last_seen', DateTime),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['iz_dnevnika_acc'].drop()
    post_meta.tables['user'].columns['username'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['iz_dnevnika_acc'].create()
    post_meta.tables['user'].columns['username'].drop()
