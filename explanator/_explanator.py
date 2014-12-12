import itertools

__author__ = 'pershik'

import random
from hb_res.explanation_source import sources_registry, ExplanationSource


SOURCES = sources_registry.sources_registered()
source_names = [s.name for s in SOURCES]

words_list = []
words_list_by_asset_name = dict()
for s in SOURCES:
    li = list(s.explainable_words())
    words_list_by_asset_name[s.name] = li
    words_list.extend(li)
words_set = frozenset(words_list)


def _apply_asset_filter(assets):
    if assets is None:
        sources_filtered = SOURCES
    elif isinstance(assets, str):
        sources_filtered = [sources_registry.source_for_name(assets)]
    else:
        sources_filtered = [sources_registry.source_for_name(name) for name in assets]
    return sources_filtered


def get_explainable_words(assets=None):
    """
    Returns an iterable of all words for which we have any explanation.

    :return: iterable
    """
    assets = _apply_asset_filter(assets)
    return itertools.chain(map(ExplanationSource.explainable_words, assets))


def get_random_word(assets=None):
    if assets is None:
        return random.choice(words_list)
    if isinstance(assets, str):
        return random.choice(words_list_by_asset_name[assets])

    lists = [words_list_by_asset_name[name] for name in assets]
    total = sum(len(list) for list in lists)
    rand = random.randrange(total)
    upto = 0
    for list in lists:
        upto += len(list)
        if rand < upto:
            return list[upto-rand]
    assert False, 'Shouldn\'t get here'


def explain_list(word, assets=None):
    """
    Returns list of tuple (Explanations, asset_name)
    """
    sources_filtered = _apply_asset_filter(assets)
    if word in words_set:
        res = list()
        for s in sources_filtered:
            res.extend(zip(s.explain(word), itertools.repeat(s.name)))
        return res
    else:
        return []


def explain(word, assets=None):
    """
    Returns tuple (Explanation, asset_name)

    :param word: a russian noun in lowercase
    :return: the explanation
    """
    if word in words_set:
        return random.choice(explain_list(word, assets))
    else:
        return None
