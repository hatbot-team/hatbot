
__all__ = [
    'get_database',
    'create_nonexistent_tables',
    'init_database',
    'Feedback'
]

from ._database import init_database, get_database
from .feedback import Feedback


def create_nonexistent_tables():
    tables = (
        Feedback,
    )

    get_database().create_tables(tables, safe=True)
