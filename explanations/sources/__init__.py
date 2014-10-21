__author__ = 'moskupols'

__all__ = [
    'ExplanationSource',
    'GapExplanationSource',
    'AntonymSource',
    'SynonymSource'
    'CollocationsSource',
    'PhraseologicalSource',
    'FilmTitlesSource'
    'DefinitionSource',
    'CrosswordSource'
]

from .ExplanationSource import ExplanationSource
from .GapExplanationSource import GapExplanationSource
from .collocations import CollocationsSource
from .phraseological import PhraseologicalSource
from .film_titles import FilmTitlesSource
from .antonyms import AntonymSource
from .synonyms import SynonymSource
from .definitions import DefinitionSource
from .crosswords import CrosswordSource
