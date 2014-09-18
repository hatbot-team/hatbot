__author__ = 'moskupols'

from lang_utils.morphology import get_initial_forms

def are_cognates(a, b):
    """
    Checks two words for having same root.

    Being a stub, currently it always returns False.

    >>> are_cognates('мама', 'рама')
    False
    >>> are_cognates('мама', 'маме')
    True

    :param a: string containing russian word
    :param b: same as a
    :return: True if a and b are cognates, False otherwise.
    """
    return not set(get_initial_forms(a)).isdisjoint(get_initial_forms(b))
