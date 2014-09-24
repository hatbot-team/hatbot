__author__ = 'moskupols'

import random
from explanations.sources import CollocationsSource, PhraseologicalSource
from explanations import Explanation

words = set(CollocationsSource.explainable_words())
words.update(PhraseologicalSource.explainable_words())
words_list = list(words)


def get_explainable_words():
    """
    Returns an iterable of all words for which we have any explanation.

    :return: iterable
    """
    return words


def get_random_word():
    return random.choice(words_list)


def explain(word) -> Explanation:
    """
    Returns the best explanation of the given word.

    :param word: a russian noun in lowercase
    :return: the explanation
    """
    if word in words:
        return random.choice(CollocationsSource.explain(word) + PhraseologicalSource.explain(word))
    else:
        return None
