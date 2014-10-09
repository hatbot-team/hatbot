import codecs
import os
from sys import stderr

from lang_utils.cognates.cognates import are_cognates
from lang_utils.morphology.word_forms import get_valid_noun_initial_form
from lang_utils.morphology.parts_of_speech import get_parts_of_speech
from explanations.sources.synonyms._synonyms_quality import \
    choose_best_synonyms


__author__ = 'skird'

BASE_FILENAME = 'synonyms.txt'
SYNONYMS_BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + "/" + BASE_FILENAME

VALID_PARTS = {'NOUN', 'ADJF', 'ADJS', 'COMP', 'VERB',
               'INFN', 'PRTF', 'PRTS', 'GRND', 'NUMR', 'ADVB', 'NPRO'}


def init_base():
    try:
        _database = codecs.open(SYNONYMS_BASE_PATH, 'r', encoding='utf-8')
    except FileNotFoundError:
        stderr.write('Synonyms dictionary doesn\'t exist\n')
        return
    global full_synonyms_list
    for line in _database:
        words = line.split()
        new_initial = get_valid_noun_initial_form(words[0])
        if new_initial is not None:
            new_list = []
            for synonym in words[1::]:
                if are_cognates(new_initial, synonym):
                    continue
                valid_part = False
                for part in get_parts_of_speech(synonym):
                    if part in VALID_PARTS:
                        valid_part = True
                if valid_part:
                    new_list.append(synonym)
            if len(new_list) != 0:
                if new_initial in full_synonyms_list.keys():
                    full_synonyms_list[new_initial].extend(new_list)
                else:
                    full_synonyms_list[new_initial] = new_list


def build_explanations():
    global full_synonyms_list
    for word, synonyms_list in full_synonyms_list.items():
        noun_id[word] = len(synonyms)
        best_synonyms = choose_best_synonyms(word, synonyms_list)
        initial_words.append(word)
        synonyms.append(best_synonyms)


noun_id = dict()
synonyms = []
initial_words = []
full_synonyms_list = dict()

init_base()
build_explanations()