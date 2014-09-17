__author__ = 'Алексей'

try:
    from . import _collocations_base
except SystemError:
    import _collocations_base

from explanations.sources.ExplanationSource import ExplanationSource

class CollocationsSource(ExplanationSource):

    @classmethod
    def keys_for(cls, word):
        """
        Explains meaning of word with the help of collocation base.
        :param word: initial word to explain
        :return: List of explanations
        Example:
        >>> CollocationsSource.keys_for('учёт')
        ['миграционного *пропуск*']
        >>> CollocationsSource.keys_for('язык')
        ['русском *пропуск*']
        """
        if word in _collocations_base.expl_collocation:
            return [e for e in _collocations_base.expl_collocation[word]]
        else:
            return []

    @classmethod
    def represent_explanation(cls, key):
        return "Заполни пропуск и поставь слово в начальную форму: " + key

    @classmethod
    def explainable_words(cls):
        """
        Gives all explainable words
        :return: Set with all explainable with collocation words
        """
        return _collocations_base.expl_collocation.keys()
