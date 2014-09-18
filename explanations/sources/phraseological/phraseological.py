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
        Explains meaning of the word with the help of phraseological base
        :param word: word to explain
        :return: list of explanations
        Example:
        >>> PhraseologicalSource.keys_for('голод')
        [(204, 0)]
        >>> PhraseologicalSource.keys_for('полка')
        [(422, 3), (729, 3)]
        """
        if word in _phraseological_base.keys_dict.keys():
            return [k for k in _phraseological_base.keys_dict[word]]
        else:
            return []

    @classmethod
    def gap_prefix(cls, key):
        return ' '.join(_phraseological_base.accepted_phrases[key[0]][:key[1]])

    @classmethod
    def gap_suffix(cls, key):
        return ' '.join(_phraseological_base.accepted_phrases[key[0]][key[1] + 1:])

    @classmethod
    def explainable_words(cls):
        return _phraseological_base.keys_dict.keys()
