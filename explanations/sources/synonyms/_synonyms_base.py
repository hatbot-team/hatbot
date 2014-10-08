import codecs
import os
from sys import stderr

from lang_utils.cognates.cognates import are_cognates
from lang_utils.morphology.word_forms import get_valid_noun_initial_form


__author__ = 'skird'

BASE_FILENAME = 'synonyms.txt'
SYNONYMS_BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/" + BASE_FILENAME


def init_base():
    try:
        _database = codecs.open(SYNONYMS_BASE_PATH, 'r', encoding='utf-8')
    except FileNotFoundError:
        stderr.write('Synonyms dictionary doesn\'t exist\n')
        return
    global synonyms, initial_words
    for line in _database:
        words = line.split()

        new_initial = get_valid_noun_initial_form(words[0])
        if new_initial is not None:
            new_list = [w for w in words[1::] if not are_cognates(new_initial, w)]
            if len(new_list) != 0:
                noun_id[new_initial] = len(synonyms)
                synonyms.append(new_list)
                initial_words.append(new_initial)
        else:
            synonyms.append(None)
            initial_words.append(None)

noun_id = dict()
synonyms = []
initial_words = []

init_base()
