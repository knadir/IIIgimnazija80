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


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['iz_dnevnika_acc'].drop()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    pre_meta.tables['iz_dnevnika_acc'].create()
