__author__ = 'skird'

try:
    from . import _synonyms_base
except SystemError:
    import _synonyms_base


# noinspection PyProtectedMember
def get_synonyms(word):
    """
    Get synonyms list for the given word
    :param word - russian word in the initial form
    :return - list of all its synonyms

    Use case:

    >>> get_synonyms('богомолье')
    ['богослужение', 'священнодействие']
    >>> get_synonyms('адский')
    ['невыносимый', 'каторжный', 'дьявольский', 'сатанинский', 'анафемский', 'инфернальный']

    """

    if word in _synonyms_base._synonyms:
        return _synonyms_base._synonyms[word]
    else:
        return []