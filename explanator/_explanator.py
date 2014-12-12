__author__ = 'pershik, ryad0m, keksozavr'

from hb_res.explanations import Explanation
import random
from hb_res.explanation_source import sources_registry


SOURCES = sources_registry.sources_registered()
SELECTED_FILE = open("explanator/goodwords.dat", 'r', encoding='utf-8')

goodwordslist = []
for s in SELECTED_FILE:
    goodwordslist.append(s.strip())


asset_by_key = dict()
words = set()
for s in SOURCES:
    for word in s.explainable_words():
        words.add(word)
        explanations = s.explain(word)
        for explanation in explanations:
            asset_by_key[explanation.key] = s.name
words_list = list(words)


def get_explainable_words():
    """
    Returns an iterable of all words for which we have any explanation.

    :return: iterable
    """
    return words


def get_random_word(selected=False):
    if (selected):
        return random.choice(goodwordslist)
    return random.choice(words_list)


def explain_list(word):
    """
    Returns list of tuple (Explanations, asset_name)
    """
    if word in words:
        res = list()
        for s in SOURCES:
            explanations = s.explain(word)
            for explanation in explanations:
                res.append((explanation, asset_by_key[explanation.key]))
        return res
    else:
        return None


def explain(word):
    """
    Returns tuple (Explanation, asset_name)

    :param word: a russian noun in lowercase
    :return: the explanation
    """
    if word in words:
        return random.choice(explain_list(word))
    else:
        return None
