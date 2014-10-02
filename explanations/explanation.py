__author__ = 'moskupols'

from explanations import sources_registry
import json


class Explanation:
    """
    The class identifying a single explanation and giving access to its text.

    It stores an explanation source name and a key to distinguish this very explanation from others
     from this very source. The source has to be registered in sources_registry.

    Probably the most important usages are obtaining the explanation text...
    >>> from explanations import Explanation
    >>> e = sources_registry.source_for_name('CollocationsSource').explain('суд')[0]
    >>> e.text
    'конституционный *пропуск*'
    >>> str(e)
    'конституционный *пропуск*'
    >>> e
    Explanation(source="CollocationsSource", key=(25, 1))

    ... and JSON serializing and de-serializing (notice that JSON version does not include text):
    >>> import json
    >>> e = sources_registry.source_for_name('SynonymSource').explain('пробст')[0]
    >>> e_dumped = json.dumps(e.json_serializable(), sort_keys=True, indent='\t')
    >>> print(e_dumped)
    {
       "__type__": "Explanation",
       "key": "\u043f\u0440\u043e\u0431\u0441\u0442",
       "source": "SynonymSource"
    }
    >>> json.loads(e_dumped, object_hook=Explanation.decode_json)
    Explanation(source="SynonymSource", key=пробст)
    >>> e2 = sources_registry.source_for_name('PhraseologicalSource').explain('час')[0]
    >>> json.dumps([e, e2], sort_keys=True)
    Traceback (most recent call last):
    ...
    TypeError: Explanation(source="SynonymSource", key=пробст) is not JSON serializable
    >>> pair_dumped = json.dumps([e, e2], cls=Explanation.JsonEncoder, sort_keys=True, indent='\t')
    >>> print(pair_dumped)
    [
     {
      "__type__": "Explanation",
      "key": "\u043f\u0440\u043e\u0431\u0441\u0442",
      "source": "SynonymSource"
     },
     {
      "__type__": "Explanation",
      "key": [
       40,
       1
      ],
      "source": "PhraseologicalSource"
     }
    ]
    >>> print(json.loads(pair_dumped, object_hook=Explanation.decode_json))
    [Explanation(source="SynonymSource", key=пробст), Explanation(source="PhraseologicalSource", key=[40, 1])]

    It also supports hashing and equality check (iff key supports it).
    """

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
                return {
                    '__type__': 'Explanation',
                    'source': o.source_name,
                    'key': o.key
                }
            return json.JSONEncoder.default(self, o)

    def json_serializable(self):
        return Explanation.JsonEncoder().default(self)

    @staticmethod
    def decode_json(dct):
        """
        Tries to convert the given dict to an Explanation, checking that it was
        previously generated for using with JSON.

        :param dct: the dict
        :return: Explanation if success, dct otherwise
        """
        if dct.get('__type__', "").endswith('Explanation'):
            return Explanation(dct['source'], dct['key'])
        return dct
