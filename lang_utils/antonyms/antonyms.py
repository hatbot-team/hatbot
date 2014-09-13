# coding:utf8

__author__ = 'pershik'

try:
    from . import _init_antonyms
except SystemError:
    import _init_antonyms


def get_antonyms(word):

    """
    Get antonyms list for the given word

    >>> get_antonyms('свет')
    ['тьма', 'мрак', 'темнота', 'тень']
    >>> get_antonyms('диван')
    []

    :param word: russian word in the initial form
    :return: list of all its antonyms
    """
    if word in _init_antonyms.antonyms:
        return _init_antonyms.antonyms[word]
    else:
        return []
