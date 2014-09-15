__author__ = 'moskupols'

import random
from explanations import collocations

word_to_explanations = collocations.get_all_explanations()


def get_explainable_words():
    """
    Returns an iterable of all words for which we have any explanation.

    :return: iterable
    """
    return word_to_explanations.keys()


def explain(word) -> str:
    """
    Returns the best explanation of the given word.

    :param word: a russian noun in lowercase
    :return: the explanation
    """
    if word in word_to_explanations:
        return random.choice(word_to_explanations[word])
    else:
        return None
