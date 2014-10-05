__author__ = 'Алексей'

from explanations.sources.phraseological._phraseological_base \
    import keys_dict, phrases_list
from explanations.sources.GapExplanationSource import GapExplanationSource
from explanations import sources_registry


class PhraseologicalSource(GapExplanationSource):

    def __init__(self):
        super().__init__('PhraseologicalSource')

    @classmethod
    def keys_for_word(cls, word):
        """
        Returns keys enough to recover the explanation text
        :param word: word to explain
        :return: list of explanation keys
        Example:
        >>> PhraseologicalSource.keys_for_word('голод')
        [(228, 0)]
        >>> PhraseologicalSource.keys_for_word('полка')
        [(472, 3), (835, 3)]
        """
        if word in keys_dict.keys():
            return [k for k in keys_dict[word]]
        else:
            return []

    @classmethod
    def before_gap(cls, key):
        return ' '.join(phrases_list[key[0]][:key[1]])

    @classmethod
    def after_gap(cls, key):
        return ' '.join(phrases_list[key[0]][key[1] + 1:])

    @classmethod
    def explainable_words(cls):
        return keys_dict.keys()

sources_registry.register_source(PhraseologicalSource())
