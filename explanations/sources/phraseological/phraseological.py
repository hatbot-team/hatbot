__author__ = 'Алексей'

try:
    from . import _phraseological_base
except SystemError:
    import _phraseological_base

from explanations.sources.GapExplanationSource import GapExplanationSource


class PhraseologicalSource(GapExplanationSource):

    @classmethod
    def keys_for(cls, word):
        """
        Returns keys enough to recover the explanation text
        :param word: word to explain
        :return: list of explanation keys
        Example:
        >>> PhraseologicalSource.keys_for('голод')
        [(228, 0)]
        >>> PhraseologicalSource.keys_for('полка')
        [(472, 3), (835, 3)]
        """
        if word in _phraseological_base.keys_dict.keys():
            return [k for k in _phraseological_base.keys_dict[word]]
        else:
            return []

    @classmethod
    def gap_prefix(cls, key):
        return ' '.join(_phraseological_base.phrases_list[key[0]][:key[1]])

    @classmethod
    def gap_suffix(cls, key):
        return ' '.join(_phraseological_base.phrases_list[key[0]][key[1] + 1:])

    @classmethod
    def explainable_words(cls):
        return _phraseological_base.keys_dict.keys()
