import codecs

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
    global antonyms
    for line in antonyms_file:
        words = line.strip().split('-')
        antonyms[words[0]] = words[1].split(',')


antonyms = dict()
init_antonyms()
