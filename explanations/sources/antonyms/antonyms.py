# coding:utf8
from explanations.sources import ExplanationSource
from explanations.sources_registry import register_source

__author__ = 'pershik'

from explanations.sources.antonyms import _antonyms_base

class AntonymSource(ExplanationSource):

    def __init__(self):
        super().__init__('AntonymSource')

    @classmethod
    def explainable_words(cls):
        """
        :return: iterable containing all russian nouns which have at least one antonym
        """
        return _antonyms_base.keys_dict.keys()

    @classmethod
    def keys_for_word(cls, word):
        i = _antonyms_base.keys_dict.get(word)
        return [] if i is None else [i]

    @classmethod
    def text_for_key(cls, key):
        antonyms = _antonyms_base.antonym_lists[key]
        if len(antonyms) == 1:
            return 'антоним к слову ' + antonyms[0]
        return 'антоним к словам ' + ', '.join(antonyms)

    @classmethod
    def get_antonyms(cls, word: str)->list:

        """
        Get antonyms list for the given word.

        >>> from explanations.sources import AntonymSource
        >>> AntonymSource.get_antonyms('свет')
        ['тьма', 'мрак', 'темнота', 'тень']
        >>> AntonymSource.get_antonyms('диван')
        []

        :param word: russian word in the initial form, in lowercase
        :return: list of all its antonyms
        """
        i = _antonyms_base.keys_dict.get(word)
        if i is not None:
            return _antonyms_base.antonym_lists[i][:]
        else:
            return []

register_source(AntonymSource())
