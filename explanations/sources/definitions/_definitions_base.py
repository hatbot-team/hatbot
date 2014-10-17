__author__ = 'skird'

from lang_utils.morphology import get_parts_of_speech
from lang_utils.cognates import are_cognates

from sys import stderr
import os
import re
import codecs

DEFINITIONS_DATABASE_PATH = \
    os.path.dirname(os.path.abspath(__file__)) + '/definitions.txt'

DELIMITERS_REGEXP = '[\W\(\);:.,]+'
GAP_WORD = '*пропуск*'
GAP_CODE = '###'


def add_definition(word, definition_id, definition_text):
    """
    This method tries to add an explanation from parsed definitions database

    It checks if a word is a NOUN.

    Note: that there is no checks (they are too slow)
    Database must be preprocessed not to contain such definitions

    :param word: word to define
    :param definition_id unique key for each explanation is stored in database for persistence
    :param definition_text text of definition
    """
    global keys_list
    global definitions_dict

    word = word.lower()

    # Note: ALL CHECKS ARE DISABLED (it takes infinitely many time for initialisation)

    # if 'NOUN' not in get_parts_of_speech(word):
    #    return

    # for def_word in re.split(DELIMITERS_REGEXP, definition_text):
    #    if are_cognates(word, def_word):
    #        return

    definitions_dict[definition_id] = (word, re.sub(GAP_CODE, GAP_WORD, definition_text))
    keys_list.setdefault(word, []).append(definition_id)


def init_base():
    """
    Method uses parsed definitions file to create dict of explanations
    """
    try:
        _database = codecs.open(DEFINITIONS_DATABASE_PATH, 'r', encoding='utf-8')
    except FileNotFoundError:
        stderr.write('Definitions database doesn\'t exist\n')
        return

    for line in _database:
        tokens = line.strip().split()
        word, num_exp = tokens[0], int(tokens[1])
        for i in range(num_exp):
            tokens = _database.readline().strip().split('@')
            def_id, text = int(tokens[0]), tokens[1]
            add_definition(word, def_id, text)


definitions_dict = dict()
keys_list = dict()

init_base()
