__author__ = 'pershik'

from . import _init_antonyms


def get_antonyms(word):
    if word in _init_antonyms.antonyms:
        return _init_antonyms.antonyms[word]
    else:
        return []
