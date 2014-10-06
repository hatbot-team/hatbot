__author__ = 'moskupols'

__all__ = ['get_parts_of_speech', 'get_initial_forms', 'get_noun_initial_form', 'morph']

import pymorphy2
morph = pymorphy2.MorphAnalyzer()

from .parts_of_speech import get_parts_of_speech
from .word_forms import get_initial_forms, get_noun_initial_form
