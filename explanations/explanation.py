__author__ = 'moskupols'

from . import sources_registry
import json


class Explanation:

    def __init__(self, source, key):
        if not source in sources_registry.sources_registered() and\
           not source in sources_registry.names_registered():
            raise KeyError("Unknown source {}, register it with sources_registry".format(source))
        if not isinstance(source, str):
            source = sources_registry.name_for_source(source)

        self.source_name = source
        self.key = key

    def __repr__(self):
        return 'Explanation(source="{}", key={})'.format(self.source_name, self.key)

    def __str__(self):
        return self.text

    def __eq__(self, other):
        return isinstance(other, Explanation) and self.source_name == other.source_name

    def __hash__(self):
        return hash((self.source_name, self.key))

    @property
    def text(self)->str:
        return sources_registry.source_for_name(self.source_name).text_for_key(self.key)

    class JsonEncoder(json.JSONEncoder):
        def default(self, o):
            if isinstance(o, Explanation):
                return {'__type__': 'Explanation',
                        'source': o.source_name,
                        'key': o.key}
            return json.JSONEncoder.default(self, o)
    @staticmethod
    def json_decode_hook(dct):
        if dct.get('__type__', "").endswith('Explanation'):
            return Explanation(dct['source'], dct['key'])
        return dct

    def json_serializable(self):
        return self.JsonEncoder().default(self)
