# coding:utf8
import itertools
from explanations.sources import ExplanationSource

__author__ = 'pershik'

try:
    from . import _antonyms_base
except SystemError:
    import _antonyms_base


class AntonymSource(ExplanationSource):

    @classmethod
    def explainable_words(cls):
        """
        :return: iterable containing all russian nouns which have at least one antonym
        """
        return _antonyms_base.keys_dict.keys()

    @classmethod
    def keys_for(cls, word):
        i = _antonyms_base.keys_dict.get(word)
        return [] if i is None else [i]

    @classmethod
    def represent_explanation(cls, key):
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
