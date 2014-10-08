__author__ = 'Алексей'

from explanations.sources.synonyms._synonyms_base import \
    initial_words, synonyms

MAX_EXPLANATION_SYNONYMS_NUMBER = 5


def synonyms_pair_quality(first: str, second: str):
    """
    Calculates absolute quality of a pair of synonyms
    (Not yet represented, just returns 0)
    :param first: first synonym
    :param second: second synonym
    :return: a number or any comparable object, which represents quality of synonyms pair
    """
    return 0


def choose_best_synonyms(explanation_key):
    """
    Gets best list of synonyms for synonyms explanation, represented by key
    :param explanation_key: key of synonyms explanation
    :return: list of required synonyms
    """
    synonyms_list = synonyms[explanation_key]
    word = initial_words[explanation_key]
    new_synonyms_list = synonyms_list.copy()
    new_synonyms_list.sort(key=lambda synonym: synonyms_pair_quality(word, synonym), reverse=True)
    if len(synonyms_list) > MAX_EXPLANATION_SYNONYMS_NUMBER:
        return new_synonyms_list[0:MAX_EXPLANATION_SYNONYMS_NUMBER:1]
    else:
        return new_synonyms_list