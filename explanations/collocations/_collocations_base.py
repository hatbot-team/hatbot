__author__ = 'Алексей'

import os
from lang_utils.morphology import get_initial_forms
from lang_utils.morphology import get_parts_of_speech
from lang_utils.cognates import are_cognates

COLLOCATIONS_PATH = \
    os.path.dirname(os.path.abspath(__file__)) + '/collocations.txt'

BANNED_PARTS = ['NPRO', 'PRED', 'PREP', 'CONJ', 'PRCL', 'INTJ']

def put_word_in_initial_form(word):
    return get_initial_forms(word)[0]

def try_add(initial_word, explanation_word, skip_position):
    """
    This method is to add (initial_word, explanation_word) pair into the list of explanations.
    :param initial_word: word to explain in the collocation
    :param explanation_word: another word in the collocation
    :param skip_position: number of position of initial word (0 or 1)
    Method checks if initial word is NOUN, and explanation word is preposition,
    conjunction or another minor part of speech, and adds explanation into dict
    """
    correct = True
    if are_cognates(initial_word, explanation_word):
        correct = False
    if not ('NOUN' in get_parts_of_speech(initial_word)):
        correct = False
    if get_parts_of_speech(explanation_word) == [None]:
        correct = False
    for wrong_part in BANNED_PARTS:
        if wrong_part in get_parts_of_speech(explanation_word):
            correct = False
    global expl_collocation
    if correct:
        explanation = "Заполни пропуск и поставь слово в начальную форму. "
        if skip_position == 0:
            explanation += "*пропуск* " + explanation_word
        else:
            explanation += explanation_word + " *пропуск*"
        initial_word = put_word_in_initial_form(initial_word)
        expl_collocation[initial_word] = expl_collocation.get(initial_word, [])
        expl_collocation[initial_word] += [explanation]


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

init_base()