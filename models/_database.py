import peewee

__author__ = 'moskupols'

database = peewee.Proxy()
database_url = None


def init_database(url: str='sqlite:///hatbot.sqlite'):
    """
    Initializes database connection.
    See https://peewee.readthedocs.org/en/latest/peewee/database.html?highlight=url#connecting-using-a-database-url
    for info on URL format.

    Please note that psycopg2 package has to be installed if we want to use PostgreSQL engine.

    :param url: str describing type and parameters of connection
    """
    global database, database_url
    assert database_url is None, 'database should be initialized exactly once'

    from playhouse import db_url
    database.initialize(db_url.connect(url))
    database.connect()
    database_url = url


def get_database()->peewee.Database:
    return database
