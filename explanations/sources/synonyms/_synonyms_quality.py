__author__ = 'Алексей'

MAX_EXPLANATION_SYNONYMS_NUMBER = 5


def synonyms_pair_quality(first: str, second: str):
    """
    Calculates absolute quality of a pair of synonyms: number from [0, 100]
    (Not yet represented, just returns 0)
    :param first: first synonym
    :param second: second synonym
    :return: a number or any comparable object, which represents quality of synonyms pair
    """
    return 0


def choose_best_synonyms(word, synonyms_list):
    """
    Gets best list of synonyms to explain word from synonym_list
    :param word: word to explain
    :param: synonym_list: list of it's synonyms to choose from
    :return: list of required synonyms
    """
    new_synonyms_list = synonyms_list.copy()
    new_synonyms_list.sort(key=lambda synonym: synonyms_pair_quality(word, synonym), reverse=True)
    if len(synonyms_list) > MAX_EXPLANATION_SYNONYMS_NUMBER:
        return new_synonyms_list[0:MAX_EXPLANATION_SYNONYMS_NUMBER:1]
    else:
        return new_synonyms_list


def synonyms_priory_rate(word, synonym_list):
    values = [synonyms_pair_quality(word, synonym) for synonym in synonym_list]
    return sum(values) / len(values)