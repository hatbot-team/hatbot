__author__ = 'Алексей'

import os
from lang_utils.morphology import get_initial_forms
from lang_utils.morphology import get_parts_of_speech
from lang_utils.cognates import are_cognates

COLLOCATIONS_PATH = \
    os.path.dirname(os.path.abspath(__file__)) + '/collocations.txt'

BANNED_PARTS = {'NPRO', 'PRED', 'PREP', 'CONJ', 'PRCL', 'INTJ'}

def get_noun_initial_form(word):
    possible_forms = get_initial_forms(word, {'NOUN'})
    if len(possible_forms) == 0:
        return None
    else:
        return possible_forms[0]

def try_add(words, skip_position):
    """
    This method is to add (initial_word, explanation_word) pair into the list of explanations.
    :param words: list of the two words of the collocation
    :param skip_position: position of initial word int the collocation(0 or 1)
    Method checks if initial word is NOUN, and explanation word is preposition,
    conjunction or another minor part of speech, and adds explanation into dict
    """
    global keys_dict
    global collocations_list
    if skip_position == 0:
        collocations_list.append(None)

    initial_word = words[skip_position]
    explanation_word = words[1-skip_position]

    initial_word = get_noun_initial_form(initial_word)
    if initial_word is None:
        return
    if are_cognates(initial_word, explanation_word):
        return
    list_of_explanation_parts = get_parts_of_speech(explanation_word)
    if len(list_of_explanation_parts) == 0:
        return
    if not BANNED_PARTS.isdisjoint(list_of_explanation_parts):
        return

    if collocations_list[-1] is None:
        collocations_list[-1] = words
    keys_dict.setdefault(initial_word, []).append((len(collocations_list) - 1, skip_position))


def init_base():
    """
    Parses initial collocation file and adds pair to dict
    """
    raw_data = open(COLLOCATIONS_PATH)
    for line in raw_data:
        words = line.split()
        try_add(words[:2], 0)
        try_add(words[:2], 1)

keys_dict = dict()
collocations_list = []

init_base()
