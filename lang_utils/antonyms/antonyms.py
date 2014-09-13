__author__ = 'pershik'

from . import _init_antonyms


def get_antonyms(word):
    return _init_antonyms.antonyms[word]
