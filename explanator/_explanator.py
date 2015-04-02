import itertools
import random

from hb_res.explanation_source import sources_registry, ExplanationSource


__author__ = 'pershik, ryad0m, keksozavr'

ALL_SOURCES = sources_registry.sources_registered()
ALL_SOURCES_NAMES_SET = frozenset(sources_registry.names_registered())

words_list = []
words_list_by_source_name = dict()
for s in ALL_SOURCES:
    li = list(s.explainable_words())
    words_list_by_source_name[s.name] = li
    words_list.extend(li)
words_set = frozenset(words_list)

SELECTED_SOURCE = sources_registry.source_for_name('Selected')
SELECTION_LEVELS = {'good', 'all'}


def _pick_sources_by_names(names):
    if names is None:
        sources_filtered = ALL_SOURCES
    else:
        if isinstance(names, str):
            names = [names]
        sources_filtered = [sources_registry.source_for_name(name) for name in names]
    return sources_filtered


def get_explainable_words(sources=None):
    """
    Returns an iterable of all words for which we have any explanation.

    :return: iterable
    """
    sources = _pick_sources_by_names(sources)
    return itertools.chain(map(ExplanationSource.explainable_words, sources))


def get_random_word(*, sources_names=None, selection_level=None):
    # assert sources_names is None or selection_level is None

    if sources_names is None:
        return random.choice(words_list
                             if selection_level == 'all'
                             else words_list_by_source_name['Selected'])

    # If the user wants a sole specific asset, the task is straightforward
    if not isinstance(sources_names, str) and len(sources_names) == 1:
        sources_names = sources_names[0]
    if isinstance(sources_names, str):
        return random.choice(words_list_by_source_name[sources_names])

    # otherwise we have to pick a uniformly random element from several lists,
    # but we wouldn't like to join them, as they are long
    lists = [words_list_by_source_name[name] for name in sources_names]
    total = sum(map(len, lists))
    rand = random.randrange(total)
    upto = 0
    for word_list in lists:
        upto += len(word_list)
        if rand < upto:
            return word_list[rand - upto]  # yep, negative indexation
    assert False, 'Shouldn\'t get here'


def explain_list(word, sources_names=None):
    """
    Returns list of tuple (Explanations, asset_name)
    """
    if word in words_set:
        sources_filtered = _pick_sources_by_names(sources_names)
        res = list()
        for s in sources_filtered:
            res.extend(zip(s.explain(word), itertools.repeat(s.name)))
        random.shuffle(res)
        return res
    else:
        return []


def explain(word, sources_names=None):
    """
    Returns tuple (Explanation, asset_name)

    :param word: a russian noun in lowercase
    :return: the explanation
    """
    if word in words_set:
        return explain_list(word, sources_names)[0]
    else:
        return None
