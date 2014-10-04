__author__ = 'Алексей'

try:
    from . import _collocations_base
except SystemError:
    import _collocations_base

from explanations.sources.GapExplanationSource import GapExplanationSource

class CollocationsSource(GapExplanationSource):

    @classmethod
    def keys_for_word(cls, word):
        """
        Explains meaning of word with the help of collocation base.
        :param word: initial word to explain
        :return: List of explanations
        Example:
        >>> CollocationsSource.keys_for_word('учёт')
        [(50, 1)]
        >>> CollocationsSource.keys_for_word('язык')
        [(74, 1)]
        """
        if word in _collocations_base.keys_dict:
            return list(_collocations_base.keys_dict[word])
        else:
            return []

    @classmethod
    def before_gap(cls, key):
        if key[1] == 0:
            return ''
        return _collocations_base.collocations_list[key[0]][0]

    @classmethod
    def after_gap(cls, key):
        if key[1] == 1:
            return ''
        return _collocations_base.collocations_list[key[0]][1]

    @classmethod
    def explainable_words(cls):
        """
        Gives all explainable words
        :return: Set with all explainable with collocation words
        """
        return _collocations_base.keys_dict.keys()
