__author__ = 'moskupols'

__all__ = ['CollocationsSource',
           'PhraseologicalSource',
           'ExplanationSource',
           'GapExplanationSource',
           'AntonymSource'
           ]

from .collocations import CollocationsSource
from .phraseological import PhraseologicalSource
from .ExplanationSource import ExplanationSource
from .GapExplanationSource import GapExplanationSource
from .antonyms import AntonymSource
