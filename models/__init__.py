"""
This package contains database models and access functions, all relying on peewee Object Relational Mapper that
appears to be both lightweight and expressive.

Please note that you MUST call init_database and optionally create_nonexistent_tables prior to using any model.

>>> import datetime
>>> from models import init_database, create_nonexistent_tables, Feedback
>>> init_database('sqlite:///:memory:')
>>> create_nonexistent_tables()
>>> ts1 = datetime.datetime(2014, 3, 1, 4, 1, 5, 926)
>>> ts2 = datetime.datetime(1828, 2, 7, 1, 8, 2, 8)
>>> good = Feedback(verdict='GOOD', timestamp=ts1, expl_key='some key')
>>> good.save()
1
>>> good.expl_key
'some key'
>>> viol = Feedback.create(verdict='VIOLATES', timestamp=ts2, expl_key='another key')
>>> viol.timestamp
datetime.datetime(1828, 2, 7, 1, 8, 2, 8)
>>> for f in Feedback.select().order_by(Feedback.verdict):
...     print(f.verdict, f.timestamp, f.expl_key)
GOOD 2014-03-01 04:01:05.000926 some key
VIOLATES 1828-02-07 01:08:02.000008 another key
>>> good.delete_instance()
1
>>> for entry in Feedback.raw('select count(*) as cnt from feedback'):
...     print(entry.cnt)
1
"""

__all__ = [
    'get_database',
    'create_nonexistent_tables',
    'init_database',
    'Feedback'
]

try:
    from ._database import init_database, get_database
    from .feedback import Feedback
except SystemError:
    from _database import init_database, get_database
    from feedback import Feedback


def create_nonexistent_tables():
    """
    Creates all necessary tables that do not exist yet in the database.
    """
    tables = (
        Feedback,
    )

    get_database().create_tables(tables, safe=True)
