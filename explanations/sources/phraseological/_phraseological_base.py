import codecs
from sys import stderr

__author__ = 'Алексей'

import os
from lang_utils.morphology import get_initial_forms
from lang_utils.morphology import get_parts_of_speech
from lang_utils.cognates import are_cognates

PHRASEOLOGICAL_PATH = \
    os.path.dirname(os.path.abspath(__file__)) + '/phraseologism.txt'

VALID_PARTS = {'NOUN', 'ADJF', 'ADJS', 'COMP', 'VERB',
               'INFN', 'PRTF', 'PRTS', 'GRND', 'NUMR', 'ADVB', 'NPRO'}


def get_noun_initial_form(word):
    possible_forms = get_initial_forms(word, {'NOUN'})
    if len(possible_forms) == 0:
        return None
    else:
        return possible_forms[0]

def try_add(phrase):
    """
    This method tries to add an explanation from parsed phraseological unit phrase
    for all nouns in it.
    It checks if a word is a NOUN, is there any cognates in other part,
    is there any information in the rest of phrase: at least one major part of speech
    :param phrase: the phraseological unit. Punctuation should be separated with spaces.
    """
    global keys_dict
    global phrases_list
    phrases_list.append(None) # for keys persistence

    words = phrase.split()

    parts = tuple(map(get_parts_of_speech, words))

    n_valid = 0
    for p in parts:
        if not VALID_PARTS.isdisjoint(p):
            n_valid += 1

    if n_valid == 0:
        return

    for (index, word) in enumerate(words):
        initial_word = get_noun_initial_form(word)
        if initial_word is None:
            continue

        cognates_valid = False
        for i, that_word in enumerate(words):
            if i != index and are_cognates(word, that_word):
                break
        else:
            cognates_valid = True
        if not cognates_valid:
            continue

        if n_valid == 1 and not VALID_PARTS.isdisjoint(parts[index]):
            continue

        # everything is ok, we have an explanation of (initial_)word using our source

        # if this phrase has not yet been added to the list of accepted phrases, do it
        # by replacing the last added None with the list of phrase' words
        if phrases_list[-1] is None:
            phrases_list[-1] = words

        # registering the pair (index of phrase, index of word) as a key that is enough for
        # recovering the explanation
        keys_dict.setdefault(initial_word, []).append((len(phrases_list) - 1, index))


def init_base():
    """
    Method uses parsed phraseological units file to create dict of explanations
    """
    try:
        raw_data = codecs.open(PHRASEOLOGICAL_PATH, 'r', encoding='cp1251')
    except:
        stderr.write('Phraseological base doesn\'t exist\n')
        return

    for line in raw_data:
        phrase = line.strip()
        try_add(phrase)


keys_dict = dict()
phrases_list = []

init_base()
