from models.basemodel import BaseModel
from peewee import CharField, DateTimeField


class Feedback(BaseModel):
    verdict = CharField(10)
    timestamp = DateTimeField()
    expl_key = CharField(50)
