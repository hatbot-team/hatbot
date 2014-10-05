__author__ = 'moskupols'

__all__ = [
    'ExplanationSource',
    'GapExplanationSource',
    'AntonymSource',
    'SynonymSource'
    'CollocationsSource',
    'PhraseologicalSource',
    ]

from .ExplanationSource import ExplanationSource
from .GapExplanationSource import GapExplanationSource
from .collocations import CollocationsSource
from .phraseological import PhraseologicalSource
from .antonyms import AntonymSource
from .synonyms import SynonymSource
