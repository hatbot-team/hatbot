__author__ = 'moskupols'

import random
from explanations import ExplanationID, sources_registry


SOURCES = sources_registry.sources_registered()

words = set()
for s in SOURCES:
    words.update(s.explainable_words())
words_list = list(words)


def get_explainable_words():
    """
    Returns an iterable of all words for which we have any explanation.

    :return: iterable
    """
    return words


def get_random_word():
    return random.choice(words_list)


def explain(word) -> ExplanationID:
    """
    Returns the best explanation of the given word.

    :param word: a russian noun in lowercase
    :return: the explanation
    """
    if word in words:
        return random.choice(sum(map(lambda s: s.explain(word), SOURCES), []))
    else:
        return None
