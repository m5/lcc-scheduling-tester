"""The application's model objects"""
import sqlalchemy as sa
from sqlalchemy import orm

from schedule_box.model import meta

def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    ## Reflected tables must be defined and mapped here
    #global reflected_table
    #reflected_table = sa.Table("Reflected", meta.metadata, autoload=True,
    #                           autoload_with=engine)
    #orm.mapper(Reflected, reflected_table)
    #
    meta.Session.configure(bind=engine)
    meta.engine = engine

volunteers_table = sa.Table("volunteers", meta.metadata,
        sa.Column("id", sa.types.Integer, primary_key=True),
        sa.Column("name", sa.types.String),
        sa.Column("schedule", sa.types.Integer),
        sa.Column("prefered_number_of_hours", sa.types.Integer),
        )

datasets_table = sa.Table("datasets", meta.metadata,
        sa.Column("id", sa.types.Integer, primary_key=True),
        sa.Column("name", sa.types.String),
        )

algorithms_table = sa.Table("algorithms", meta.metadata,
        sa.Column("id", sa.types.Integer, primary_key=True),
        sa.Column("name", sa.types.String),
        sa.Column("code", sa.types.Integer),
        )

volunteers_datasets_table = sa.Table("volunteers_datasets", meta.metadata,
        sa.Column("volunteer_id", sa.types.Integer, sa.ForeignKey("volunteers.id")),
        sa.Column("dataset_id", sa.types.Integer, sa.ForeignKey("datasets.id")),
        )

class Volunteer(object): pass
class Dataset(object): pass
class Algorithm(object): pass

orm.mapper(Volunteer, volunteers_table)
orm.mapper(Dataset, datasets_table, properties = {
    'volunteers' : orm.relation(Volunteer, secondary=volunteers_datasets_table, backref='datasets')
        })
orm.mapper(Algorithm, algorithms_table)

## Non-reflected tables may be defined and mapped at module level
#foo_table = sa.Table("Foo", meta.metadata,
#    sa.Column("id", sa.types.Integer, primary_key=True),
#    sa.Column("bar", sa.types.String(255), nullable=False),
#    )
#
#class Foo(object):
#    pass
#
#orm.mapper(Foo, foo_table)


## Classes for reflected tables may be defined here, but the table and
## mapping itself must be done in the init_model function
#reflected_table = None
#
#class Reflected(object):
#    pass
