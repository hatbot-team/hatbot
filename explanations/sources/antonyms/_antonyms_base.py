import codecs

from lang_utils.cognates.cognates import are_cognates
from lang_utils.morphology.word_forms import get_valid_noun_initial_form


__author__ = 'pershik'

import os
from sys import stderr

ANTONYMS_PATH = \
    os.path.dirname(os.path.abspath(__file__)) + '/antonyms.txt'


def init_antonyms():
    try:
        antonyms_file = codecs.open(ANTONYMS_PATH, 'r', encoding='utf-8')
    except FileNotFoundError:
        stderr.write('Antonyms dictionary doesn\'t exist\n')
        return
    global keys_dict
    for line in antonyms_file:
        words = line.strip().split('-')

        new_initial = get_valid_noun_initial_form(words[0])
        if new_initial is not None:
            new_list = [w for w in words[1].split(',') if not are_cognates(new_initial, w)]
            if len(new_list) != 0:
                keys_dict[new_initial] = len(antonym_lists)
                antonym_lists.append(new_list)
                initial_word.append(new_initial)
        else:
            antonym_lists.append(None)
            initial_word.append(None)


initial_word = []
antonym_lists = []
keys_dict = dict()
init_antonyms()
