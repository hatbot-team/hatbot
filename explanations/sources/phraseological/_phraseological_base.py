__author__ = 'Алексей'

import os
from lang_utils.morphology import get_initial_forms
from lang_utils.morphology import get_parts_of_speech
from lang_utils.cognates import are_cognates

PHRASEOLOGICAL_PATH = \
    os.path.dirname(os.path.abspath(__file__)) + '/phraseologism.txt'

VALID_PARTS = ['NOUN', 'ADJF', 'ADJS', 'COMP', 'VERB',
               'INFN', 'PRTF', 'PRTS', 'GRND', 'NUMR', 'ADVB', 'NPRO']


def get_noun_initial_form(word):
    possible_forms = get_initial_forms(word, {'NOUN'})
    if len(possible_forms) == 0:
        return None
    else:
        return possible_forms[0]

def try_add(phrase, index):
    """
    This method tries to add an explanation from parsed phraseological unit phrase
    for a word number index in this phrase
    It checks if a phrase[index] is a NOUN, is there any cognates in other part,
    is there any information in the rest of phrase: at least one major part of speech
    :param phrase: list of words in phraseological unit. Punctuation is also a word
    :param index: number of word we would like to explain in the phrase
    """
    initial_word = get_noun_initial_form(phrase[index])
    if initial_word is None:
        return
    n_valid = 0
    for i in range(len(phrase)):
        if i != index:
            if are_cognates(phrase[i], phrase[index]):
                return
            list_of_parts = get_parts_of_speech(phrase[i])
            valid = False
            for valid_part in VALID_PARTS:
                if valid_part in list_of_parts:
                    valid = True
            if valid:
                n_valid += 1
    if n_valid == 0:
        return
    global expl_phraseological
    global phraseological_explainable
    explanation = ""
    for i in range(len(phrase)):
        if i != index:
            explanation += phrase[i] + " "
        else:
            explanation += "*пропуск* "
    phraseological_explainable.add(initial_word)
    expl_phraseological[initial_word] = expl_phraseological.get(initial_word, [])
    expl_phraseological[initial_word] += [explanation]


def init_base():
    """
    Method uses parsed phraseological units file to create dict of explanations
    """
    raw_data = open(PHRASEOLOGICAL_PATH)
    for line in raw_data:
        phrase = line.rstrip('\n').split(' ')
        for index in range(len(phrase)):
            try_add(phrase, index)


expl_phraseological = dict()
phraseological_explainable = set()

init_base()
