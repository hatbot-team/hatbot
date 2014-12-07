"""
Describes json schemas used to communicate to clients and to store some logs.
For JSON schema spec, see, for example, http://spacetelescope.github.io/understanding-json-schema/
"""

import models

__author__ = 'moskupols'

SCHEMA_VERSION = "http://json-schema.org/schema#"

explanation_key_schema = {
    '$schema': SCHEMA_VERSION,
    'type': 'string',
    'pattern': '^[-_A-Za-z0-9]{38}==$',
}

explanation_schema = {
    '$schema': SCHEMA_VERSION,
    'type': 'object',
    'properties': {
        'id': explanation_key_schema,
        'text': {'type': 'string', 'minLength': 1},
        'word': {'type': 'string', 'minLength': 1},
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
        'verdict': {'type': 'string', 'enum': list(models.ALLOWED_VERDICTS)},
        'client_app': {'type': 'string'},
    },
    'required': ['expl_id', 'verdict', 'client_app'],
}

chat_entry_schema = {
    '$schema': SCHEMA_VERSION,
    'type': 'object',
    'properties': {
        'msecs_after_start': {'type': 'integer', 'minimum': 0},
        'actor': {'type': 'string', 'enum': ['app', 'player']},
        'text': {'type': 'string'}
    },
    'required': ['msecs_after_start', 'actor', 'text']
}

chat_log_schema = {
    '$schema': SCHEMA_VERSION,
    'type': 'object',
    'properties': {
        'client_app': {'type': 'string'},
        'word': {'type': 'string'},
        'entries': {'type': 'array', 'items': chat_entry_schema, 'uniqueItems': True},
    },
    'required': ['client_app', 'word', 'entries']
}
