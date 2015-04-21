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

ko_dolazi = Table('ko_dolazi', pre_meta,
    Column('ime_i_prezime', VARCHAR(length=50)),
    Column('razred', VARCHAR(length=4)),
)

dnevnik = Table('dnevnik', pre_meta,
    Column('id', INTEGER, primary_key=True, nullable=False),
    Column('ime_i_prezime', VARCHAR(length=50)),
    Column('razred', VARCHAR(length=4)),
    Column('ime', VARCHAR(length=15)),
    Column('prezime', VARCHAR(length=30)),
    Column('test', VARCHAR(length=30)),
)

dnevnik = Table('dnevnik', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('ime_i_prezime', String(length=50)),
    Column('razred', String(length=4)),
    Column('ime', String(length=15)),
    Column('prezime', String(length=30)),
    Column('dolazi', String(length=1)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['iz_dnevnika_acc'].drop()
    pre_meta.tables['ko_dolazi'].drop()
    pre_meta.tables['dnevnik'].columns['test'].drop()
    post_meta.tables['dnevnik'].columns['dolazi'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['iz_dnevnika_acc'].create()
    pre_meta.tables['ko_dolazi'].create()
    pre_meta.tables['dnevnik'].columns['test'].create()
    post_meta.tables['dnevnik'].columns['dolazi'].drop()
