__author__ = 'skird'

from explanations.sources.ExplanationSource import ExplanationSource
from explanations import sources_registry

# noinspection PyProtectedMember
from explanations.sources.definitions._definitions_base \
    import keys_list, definitions_dict


class DefinitionSource(ExplanationSource):
    def __init__(self):
        super().__init__('DefinitionSource')

    @classmethod
    def keys_for_word(cls, word):
        """
        Returns keys enough to recover the explanation text
        :param word: word to explain
        :return: list of explanation keys
        Example:
        >>> p = sources_registry.source_for_name('DefinitionSource')
        >>> p.keys_for_word('титр')
        [23845]
        """
        if word not in keys_list.keys():
            return []
        else:
            return [def_key for def_key in keys_list[word]]


    @classmethod
    def word_for_key(cls, key) -> str:
        """
        returns word which explanation described by key refers to
        :param key: unique key of explanation
        :return: word
        """
        return definitions_dict[key][0]

    @classmethod
    def text_for_key(cls, key):
        return definitions_dict[key][1]

    @classmethod
    def explainable_words(cls):
        """
        :return: returns iterable to all words can be explained using this source
        """
        return keys_list.keys()

sources_registry.register_source(DefinitionSource())