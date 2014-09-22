__author__ = 'Oktosha'

from lang_utils.morphology import get_initial_forms

try:
    from . import _cognates_base
except SystemError:
    import _cognates_base

def get_roots(word):
    """
    Returns list of root-words which are titles of dictionary articles containing the given word.
    If the dictionary doesn't contain the given word the list containing word itself is returned.

    :param word: russian word
    :return: list of root-words
    """
    """
    :param word:
    :return:
    """
    if word in _cognates_base.cognates:
        return _cognates_base.cognates[word]
    else:
        return [word]

def are_cognates(a, b):
    """
    Checks two words for having same root.

    >>> are_cognates('мама', 'рама')
    False
    >>> are_cognates('мама', 'маме')
    True
    >>> are_cognates('мама', 'маменька')
    True

    :param a: string containing russian word
    :param b: same as a
    :return: True if a and b are cognates, False otherwise.
    """

    a_roots = []
    for word in get_initial_forms(a):
        a_roots.extend(get_roots(word))

    b_roots = []
    for word in get_initial_forms(b):
        b_roots.extend(get_roots(word))

    return not set(a_roots).isdisjoint(b_roots)
