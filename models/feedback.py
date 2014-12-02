from models.basemodel import BaseModel
from peewee import CharField, DateTimeField

ALLOWED_VERDICTS = (
    'NOT_AN_EXPL',
    'VIOLATION',
    'NOT_IMPRESSED',
    'GOOD',
    'EXACT',
)


class Feedback(BaseModel):
    verdict = CharField(10, choices=ALLOWED_VERDICTS)
    timestamp = DateTimeField()
    expl_key = CharField(50)
