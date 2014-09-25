from sys import stderr

__author__ = 'skird'

import codecs
import os

BASE_FILENAME = 'synonyms.txt'
SYNONYMS_BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/" + BASE_FILENAME


def init_base():
    try:
        _database = codecs.open(SYNONYMS_BASE_PATH, 'r', encoding='cp1251')
    except:
        stderr.write('Synonyms dictionary doesn\'t exist\n')
        return
    global _synonyms
    for line in _database:
        words = line.split()
        _synonyms[words[0]] = words[1::]

_synonyms = dict()

init_base()
