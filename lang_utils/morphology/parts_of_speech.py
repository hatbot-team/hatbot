__author__ = 'moskupols'

try:
    from .morph import morph
except SystemError:
    from morph import morph


def get_parts_of_speech(word):
    """
    Returns a list of strings describing parts of speech the given russian word could be.
    The enums are derived from pymorphy2.

    >>> get_parts_of_speech('рогалик')
    ['NOUN']
    >>> get_parts_of_speech('постовой')
    ['ADJF', 'NOUN']
    >>> 'NOUN' in get_parts_of_speech('правил')
    True

    :param word: a russian word
    :return: list of pymorphy2 POS enums.
    """
    return list(sorted(set(p.tag.POS for p in morph.parse(word))))
