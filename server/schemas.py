import models


__author__ = 'moskupols'

SCHEMA_VERSION = "http://json-schema.org/schema#"

explanation_key_schema = {
    '$schema': SCHEMA_VERSION,
    'type': 'string',
    'pattern': '^\w{38}==$',
}

explanation_schema = {
    '$schema': SCHEMA_VERSION,
    'type': 'object',
    'properties': {
        'id': explanation_key_schema,
        'text': {'type': 'string', 'minLength': 1},
        'title': {'type': 'string', 'pattern': '[-ёа-я]+'},
        'asset': {'type': 'string', 'minLength': 1},
    },
    'required': ['id', 'text']
}

explanation_list_schema = {
    '$schema': SCHEMA_VERSION,
    'type': 'array',
    'items': explanation_schema,
}

score_feedback_schema = {
    '$schema': SCHEMA_VERSION,
    'type': 'object',
    'properties': {
        'expl_id': explanation_key_schema,
        'verdict': {'type': 'string', 'enum': list(models.ScoreFeedback.verdict.choices)},
        'client_app': {'type': 'string'},
    },
    'required': ['expl_id', 'verdict'],
}
