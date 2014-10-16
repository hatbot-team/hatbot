__author__ = 'Keks'


import os
from sys import stderr

CROSSWORDS_DATABASE_PATH = \
    os.path.dirname(os.path.abspath(__file__)) + '/crosswords.txt'

def add(word, explanation_id, explanation_text):

    global keys_list
    global crosswords_dict

    crosswords_dict[explanation_id] = (word, explanation_text)
    keys_list.setdefault(word, []).append(explanation_id)


def init_base():

    try:
        database = open(CROSSWORDS_DATABASE_PATH, 'r')
    except FileNotFoundError:
        stderr.write('Crosswords database doesn\'t exist\n')
        return

    for line in database:
        tokens = line.split('$')
        id, word, text = int(tokens[0]), tokens[1], tokens[2]
        add(word.strip().lower(), id, text.strip())


crosswords_dict = dict()
keys_list = dict()

init_base()
