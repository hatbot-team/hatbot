import peewee

__author__ = 'moskupols'

database = peewee.Proxy()
database_url = None


def init_database(url: str='sqlite:///hatbot.sqlite'):
    global database, database_url
    assert database_url is None, 'database should be initialized exactly once'

    from playhouse import db_url
    database.initialize(db_url.connect(url))
    database.connect()
    database_url = url


def get_database()->peewee.Database:
    return database
