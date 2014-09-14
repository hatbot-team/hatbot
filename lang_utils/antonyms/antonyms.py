# coding:utf8

__author__ = 'pershik'

try:
    from . import _antonyms_base
except SystemError:
    import _antonyms_base


def get_words_with_antonyms():
    """
    >>> len(get_words_with_antonyms())
    457

    :return: iterable containing all russian words which have at least one antonym
    """
    return _antonyms_base.antonyms.keys()


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
    if word in _antonyms_base.antonyms:
        return _antonyms_base.antonyms[word]
    else:
        return []
