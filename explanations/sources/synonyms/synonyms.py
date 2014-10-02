from explanations.sources import ExplanationSource

__author__ = 'skird'

try:
    from . import _synonyms_base
except SystemError:
    import _synonyms_base


class SynonymSource(ExplanationSource):
    # noinspection PyProtectedMember
    @classmethod
    def keys_for_word(cls, word: str):
        return [word] if word in _synonyms_base._nouns else []

    # noinspection PyProtectedMember
    @classmethod
    def explainable_words(cls):
        """
        :return: iterable containing all russian words which have at least one synonym
        """
        return _synonyms_base._nouns

    # noinspection PyProtectedMember
    @classmethod
    def text_for_key(cls, key):
        s = _synonyms_base._synonyms[key]
        if len(s) == 1:
            return 'синоним к слову ' + s[0]
        return 'синоним к словам ' + ', '.join(s)

    # noinspection PyProtectedMember
    def get_synonyms(word):
        """
        Get synonyms list for the given word
        :param word - russian word in the initial form
        :return - list of all its synonyms

        Use case:

        >>> from explanations.sources import SynonymSource
        >>> SynonymSource.get_synonyms('богомолье')
        ['богослужение', 'священнодействие']
        >>> SynonymSource.get_synonyms('адский')
        ['невыносимый', 'каторжный', 'дьявольский', 'сатанинский', 'анафемский', 'инфернальный']

        """
        s = _synonyms_base._synonyms.get(word)
        if s is not None:
            return list(s)
        else:
            return []
