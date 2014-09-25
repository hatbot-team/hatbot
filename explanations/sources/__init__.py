__author__ = 'moskupols'

__all__ = ['CollocationsSource',
           'PhraseologicalSource',
           'ExplanationSource',
           'GapExplanationSource',
           'AntonymSource',
           'SynonymSource'
           ]

from .collocations import CollocationsSource
from .phraseological import PhraseologicalSource
from .ExplanationSource import ExplanationSource
from .GapExplanationSource import GapExplanationSource
from .antonyms import AntonymSource
from .synonyms import SynonymSource
