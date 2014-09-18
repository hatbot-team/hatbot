__author__ = 'moskupols'

import random
from explanations.sources import CollocationsSource, PhraseologicalSource

words = set(CollocationsSource.explainable_words() + PhraseologicalSource.explainable_words())


def get_explainable_words():
    """
    Returns an iterable of all words for which we have any explanation.

    :return: iterable
    """
    return words


def explain(word) -> str:
    """
    Returns the best explanation of the given word.

    :param word: a russian noun in lowercase
    :return: the explanation
    """
    if word in words:
        return random.choice(CollocationsSource.explain(word) + PhraseologicalSource.explain(word))
    else:
        return None
