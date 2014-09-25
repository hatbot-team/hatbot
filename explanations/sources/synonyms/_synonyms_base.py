from sys import stderr
from lang_utils.morphology.parts_of_speech import get_parts_of_speech

__author__ = 'skird'

import codecs
import os

BASE_FILENAME = 'synonyms.txt'
SYNONYMS_BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/" + BASE_FILENAME


def init_base():
    try:
        _database = codecs.open(SYNONYMS_BASE_PATH, 'r', encoding='utf-8')
    except:
        stderr.write('Synonyms dictionary doesn\'t exist\n')
        return
    global _synonyms, _nouns
    for line in _database:
        words = line.split()
        _synonyms[words[0]] = words[1:]
        if 'NOUN' in get_parts_of_speech(words[0]):
            _nouns.add(words[0])

_synonyms = dict()
_nouns = set()

init_base()
