__author__ = 'moskupols'

from explanations import sources_registry


class Explanation:
    """
    The class identifying a single explanation and giving access to its text.

    It stores an explanation source name and a key to distinguish this very explanation from others
     from this very source. The source has to be registered in sources_registry.

    Probably the most important usages are obtaining the explanation text...
    >>> e = sources_registry.source_for_name('CollocationsSource').explain('суд')[0]
    >>> e.text
    'конституционный *пропуск*'
    >>> str(e)
    'конституционный *пропуск*'
    >>> e
    Explanation(source="CollocationsSource", key=(25, 1))

    ... and JSON serializing and de-serializing (notice that JSON version does not include text):
    >>> from utils import json_hooks as json
    >>> e = sources_registry.source_for_name('SynonymSource').explain('пробст')[0]
    >>> e_dumped = json.dumps(e, sort_keys=True, indent='  ')
    >>> print(e_dumped)
    {
      "py/Explanation": {
        "key": "\u043f\u0440\u043e\u0431\u0441\u0442",
        "source": "SynonymSource"
      }
    }
    >>> json.loads(e_dumped)
    Explanation(source="SynonymSource", key=пробст)
    >>> e2 = sources_registry.source_for_name('PhraseologicalSource').explain('час')[0]
    >>> pair_dumped = json.dumps([e, e2], sort_keys=True, indent='  ')
    >>> print(pair_dumped)
    [
      {
        "py/Explanation": {
          "key": "\u043f\u0440\u043e\u0431\u0441\u0442",
          "source": "SynonymSource"
        }
      },
      {
        "py/Explanation": {
          "key": {
            "py/tuple": [
              40,
              1
            ]
          },
          "source": "PhraseologicalSource"
        }
      }
    ]
    >>> print(json.loads(pair_dumped))
    [Explanation(source="SynonymSource", key=пробст), \
Explanation(source="PhraseologicalSource", key=(40, 1))]

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

    def _json_serializable(self):
        return {
            '__type__': 'Explanation',
            'source': self.source_name,
            'key': self.key
        }

    @staticmethod
    def _decode_json(dct):
        if dct.get('__type__', '') == 'Explanation':
            return Explanation(dct['source'], dct['key'])
        return dct
