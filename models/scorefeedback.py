from models.basemodel import BaseModel
from peewee import CharField, DateTimeField

ALLOWED_VERDICTS = (
    'NOT_AN_EXPL',
    'VIOLATION',
    'NOT_IMPRESSED',
    'GOOD',
    'EXACT',
)


class ScoreFeedback(BaseModel):
    verdict = CharField(20, choices=ALLOWED_VERDICTS)
    timestamp = DateTimeField()
    expl_key = CharField(50)
