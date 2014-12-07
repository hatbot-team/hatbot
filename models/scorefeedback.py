from models.basemodel import BaseModel
from peewee import CharField, DateTimeField
import datetime

ALLOWED_VERDICTS = frozenset((
    'NOT_AN_EXPL',
    'VIOLATION',
    'NOT_IMPRESSED',
    'GOOD',
    'EXACT',
))


class ScoreFeedback(BaseModel):
    verdict = CharField(20, choices=ALLOWED_VERDICTS)
    timestamp = DateTimeField(default=datetime.datetime.now)
    expl_id = CharField(50)
    client_app = CharField(null=True, default=None)
