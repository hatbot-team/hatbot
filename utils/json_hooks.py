__author__ = 'moskupols'

import json
from collections import namedtuple
from explanations import Explanation

"""
  A wrapper for standard json module that preserves *tuples* and some other classes.
  Crude but working.

  (Yeah, I know about those clever cls kwargs, but I just can't manage to make it preserve tuples)
"""


def serializable(data):
    """ Borrowed from http://robotfantastic.org/serializing-python-data-to-json-some-edge-cases.html

    :param data:
    :return:
    """
    def is_namedtuple(obj):
        """Heuristic check if an object is a namedtuple."""
        return isinstance(obj, tuple) \
               and hasattr(obj, "_fields") \
               and hasattr(obj, "_asdict") \
               and callable(obj._asdict)

    if data is None or isinstance(data, (bool, int, float, str)):
        return data
    if isinstance(data, Explanation):
        return {'py/Explanation': {
            'source': data.source_name,
            'key': serializable(data.key)
        }}
    if isinstance(data, list):
        return [serializable(val) for val in data]
    if is_namedtuple(data):
        return {'py/namedtuple': {
            "name":   type(data).__name__,
            "fields": list(data._fields),
            "values": [serializable(getattr(data, f)) for f in data._fields]
        }}
    if isinstance(data, dict):
        if all(isinstance(k, str) for k in data):
            return {k: serializable(v) for k, v in data.items()}
        return {'py/dict':
            [[serializable(k), serializable(v)] for k, v in data.items()]
        }
    if isinstance(data, tuple):
        return {"py/tuple": [serializable(val) for val in data]}
    raise TypeError("Type %s not data-serializable" % type(data))

def object_decode_hook(dct):
    """
    Tries to convert the given dict to an _DECODE_HOOKED, checking that it was
    previously generated for using with JSON.

    :param dct: the dict
    :return: encoded object on success, dct otherwise
    """
    if 'py/Explanation' in dct:
        return Explanation(**dct['py/Explanation'])
    if 'py/namedtuple' in dct:
        data = dct['py/namedtuple']
        return namedtuple(data['name'], data['fields'])(*data['values'])
    if 'py/dict' in dct:
        return dict(dct['py/dict'])
    if 'py/tuple' in dct:
        return tuple(dct['py/tuple'])

    return dct


def load(fp, **kwargs):
    kwargs['object_hook'] = object_decode_hook
    return json.load(fp, **kwargs)


def loads(s, **kwargs):
    kwargs['object_hook'] = object_decode_hook
    return json.loads(s, **kwargs)


def dump(o, fp, **kwargs):
    return json.dump(serializable(o), fp, **kwargs)


def dumps(o, **kwargs):
    return json.dumps(serializable(o), **kwargs)
