import peewee
from models._database import database

__author__ = 'moskupols'


class BaseModel(peewee.Model):
    class Meta:
        database = database
