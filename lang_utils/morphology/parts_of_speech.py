__author__ = 'moskupols'

try:
    from .morph import morph
except SystemError:
    from morph import morph


def get_parts_of_speech(word):
    """
    Returns a list strings describing parts of speech the given russian word could be.
    The enums are derived from pymorphy2.

    >>> get_parts_of_speech('рогалик')
    ['NOUN']
    >>> get_parts_of_speech('постовой')
    ['ADJF', 'NOUN']
    >>> 'NOUN' in get_parts_of_speech('правил')
    True
    >>> 'ADJF' in get_parts_of_speech('правил')
    False

    :param word: a russian word
    :return: list of pymorphy2 POS enums.
    """
    met = set()
    ret = []
    for p in morph.parse(word):
        if p.score < .1:
            continue
        pos = p.tag.POS
        if pos not in met:
            ret.append(pos)
            met.add(pos)
    return ret
