__author__ = 'moskupols'

from explanations.sources_registry import \
    source_for_name
from explanations import ExplanationRate

class Explanation:
    """
    The class identifying a single explanation and giving access to its text.

    It stores an explanation source name and a key to distinguish this very explanation from others
     from this very source. The source has to be registered in sources_registry.

    Probably the most important usages are obtaining the explanation text...
    >>> e = source_for_name('CollocationsSource').explain('суд')[0]
    >>> e.text()
    'конституционный *пропуск*'
    >>> str(e)
    'конституционный *пропуск*'
    >>> e
    Explanation(source="CollocationsSource", key=(29, 1))

    ... and JSON serializing and de-serializing (notice that JSON version does not include text):
    >>> from utils import json_hooks as json
    >>> e = source_for_name('SynonymSource').explain('пробст')[0]
    >>> e_dumped = json.dumps(e, sort_keys=True, indent='  ')
    >>> print(e_dumped)
    {
      "py/Explanation": {
        "key": 9731,
        "source": "SynonymSource"
      }
    }
    >>> json.loads(e_dumped)
    Explanation(source="SynonymSource", key=9731)
    >>> e2 = source_for_name('PhraseologicalSource').explain('час')[0]
    >>> pair_dumped = json.dumps([e, e2], sort_keys=True, indent='  ')
    >>> print(pair_dumped)
    [
      {
        "py/Explanation": {
          "key": 9731,
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
    [Explanation(source="SynonymSource", key=9731), Explanation(source="PhraseologicalSource", key=(40, 1))]

    It also supports hashing and equality check (iff key supports it).
    """

    def __init__(self, source, key):
        if isinstance(source, str):
            source = source_for_name(source)

        self.source = source
        self.key = key

    def __repr__(self):
        return 'Explanation(source="{}", key={})'.format(self.source.name, repr(self.key))

    def __str__(self):
        return self.text()

    def __eq__(self, other):
        return isinstance(other, Explanation) \
            and self.source.name == other.source_name \
            and self.key == other.key

    def __hash__(self):
        return hash((self.source.name, self.key))

    @property
    def source_name(self):
        return self.source.name

    def is_reproducible(self):
        return self.source.produces_key(self.key)

    def text(self) -> str:
        return self.source.text_for_key(self.key)

    def word(self) -> str:
        return self.source.word_for_key(self.key)

    def rate(self) -> ExplanationRate:
        return self.source.rate_for_key(self.key)