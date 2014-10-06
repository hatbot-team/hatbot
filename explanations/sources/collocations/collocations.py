from lang_utils.morphology import get_valid_noun_initial_form
from explanations.sources.GapExplanationSource import GapExplanationSource
from explanations.sources.collocations._collocations_base import \
    collocations_list, keys_dict
from explanations import sources_registry


__author__ = 'Алексей'


class CollocationsSource(GapExplanationSource):

    def __init__(self):
        super().__init__('CollocationsSource')

    @classmethod
    def keys_for_word(cls, word):
        """
        Explains meaning of word with the help of collocation base.
        :param word: initial word to explain
        :return: List of explanations
        Example:
        >>> c = sources_registry.source_for_name('CollocationsSource')
        >>> c.keys_for_word('учёт')
        [(50, 1)]
        >>> c.keys_for_word('язык')
        [(74, 1)]
        """
        if word in keys_dict:
            return list(keys_dict[word])
        else:
            return []

    @classmethod
    def word_for_key(cls, key):
        return get_valid_noun_initial_form(collocations_list[key[0]][key[1]])

    @classmethod
    def before_gap(cls, key):
        if key[1] == 0:
            return ''
        return collocations_list[key[0]][0]

    @classmethod
    def after_gap(cls, key):
        if key[1] == 1:
            return ''
        return collocations_list[key[0]][1]

    @classmethod
    def explainable_words(cls):
        """
        Gives all explainable words
        :return: Set with all explainable with collocation words
        """
        return keys_dict.keys()

sources_registry.register_source(CollocationsSource())
