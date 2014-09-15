__author__ = 'Алексей'

import os
from lang_utils.morphology import get_initial_forms
from lang_utils.morphology import get_parts_of_speech
from lang_utils.cognates import are_cognates

COLLOCATIONS_PATH = \
    os.path.dirname(os.path.abspath(__file__)) + '/collocations.txt'

BANNED_PARTS = ['NPRO', 'PRED', 'PREP', 'CONJ', 'PRCL', 'INTJ']

def get_noun_initial_form(word):
    possible_forms = get_initial_forms(word, {'NOUN'})
    if len(possible_forms) == 0:
        return None
    else:
        return possible_forms[0]

def try_add(initial_word, explanation_word, skip_position):
    """
    This method is to add (initial_word, explanation_word) pair into the list of explanations.
    :param initial_word: word to explain in the collocation
    :param explanation_word: another word in the collocation
    :param skip_position: number of position of initial word (0 or 1)
    Method checks if initial word is NOUN, and explanation word is preposition,
    conjunction or another minor part of speech, and adds explanation into dict
    """
    initial_word = get_noun_initial_form(initial_word)
    if initial_word is None:
        return
    if are_cognates(initial_word, explanation_word):
        return
    list_of_explanation_parts = get_parts_of_speech(explanation_word)
    if list_of_explanation_parts == [None]:
        return
    for wrong_part in BANNED_PARTS:
        if wrong_part in list_of_explanation_parts:
            return
    global expl_collocation
    global collocation_explainable
    explanation = ""
    if skip_position == 0:
        explanation += "*пропуск* " + explanation_word
    else:
        explanation += explanation_word + " *пропуск*"
    expl_collocation[initial_word] = expl_collocation.get(initial_word, [])
    expl_collocation[initial_word] += [explanation]
    collocation_explainable.add(initial_word)


def init_base():
    """
    Parses initial collocation file and adds pair to dict
    """
    raw_data = open(COLLOCATIONS_PATH)
    for line in raw_data:
        words = line.split()
        try_add(words[0], words[1], 0)
        try_add(words[1], words[0], 1)

expl_collocation = dict()
collocation_explainable = set()

init_base()