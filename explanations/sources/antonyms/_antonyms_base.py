import codecs

from lang_utils.cognates.cognates import are_cognates
from lang_utils.morphology.word_forms import get_noun_initial_form


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
        antonym_lists.append(words[1].split())
        noun = get_noun_initial_form(words[0])
        if noun is not None:
            words[0] = noun
            keys_dict[noun] = len(antonym_lists) - 1
            antonym_lists[-1] = list(filter(lambda w: not are_cognates(noun, w), antonym_lists[-1]))
        initial_word.append(noun)


initial_word = []
antonym_lists = []
keys_dict = dict()
init_antonyms()
