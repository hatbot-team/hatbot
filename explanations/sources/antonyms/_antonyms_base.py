import codecs
from lang_utils.cognates.cognates import are_cognates
from lang_utils.morphology.parts_of_speech import get_parts_of_speech

__author__ = 'pershik'

import os
from sys import stderr

ANTONYMS_PATH = \
    os.path.dirname(os.path.abspath(__file__)) + '/antonyms.txt'


def init_antonyms():
    try:
        antonyms_file = codecs.open(ANTONYMS_PATH, 'r', encoding='utf-8')
    except:
        stderr.write('Antonyms dictionary doesn\'t exist\n')
        return
    global keys_dict
    for line in antonyms_file:
        words = line.strip().split('-')
        if 'NOUN' in get_parts_of_speech(words[0]):
            keys_dict[words[0]] = len(antonym_lists)
        antonym_lists.append([w for w in words[1].split(',') if not are_cognates(words[0], w)])


antonym_lists = []
keys_dict = dict()
init_antonyms()
