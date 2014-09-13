__author__ = 'moskupols'

__all__ = ['get_parts_of_speech', 'get_initial_forms', 'morph']

from .morph import morph
from .parts_of_speech import get_parts_of_speech
from .word_forms import get_initial_forms
