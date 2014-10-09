# noinspection PyProtectedMember
from explanations.sources.synonyms._synonyms_base import \
    initial_words, synonyms, noun_id, full_synonyms_list
from explanations.sources_registry import register_source
from explanations.sources import ExplanationSource
from explanations import ExplanationRate
from explanations.sources.synonyms._synonyms_quality import \
    synonyms_priory_rate

__author__ = 'skird'

DEFAULT_SOURCE_RATE = 20


class SynonymSource(ExplanationSource):

    def __init__(self):
        super().__init__('SynonymSource')

    @classmethod
    def word_for_key(cls, key) -> str:
        return initial_words[key]

    @classmethod
    def keys_for_word(cls, word: str):
        k = noun_id.get(word, None)
        return [k] if k is not None else []

    @classmethod
    def explainable_words(cls):
        """
        :return: iterable containing all russian words which have at least one synonym
        """
        return full_synonyms_list.keys()

    @classmethod
    def text_for_key(cls, key):
        s = synonyms[key]
        if len(s) == 1:
            return 'синоним к слову ' + s[0]
        return 'синоним к словам ' + ', '.join(s)

    @classmethod
    def rate_for_key(cls, key)->ExplanationRate:
        return ExplanationRate(priory_rate=synonyms_priory_rate(initial_words[key], synonyms[key]),
                               source_rate=DEFAULT_SOURCE_RATE)

    @staticmethod
    def get_synonyms(word: str)->list:
        """
        Get all available synonyms for given word

        >>> from explanations.sources import SynonymSource
        >>> SynonymSource.get_synonyms('басня')
        ['сомнение', 'побасенка', 'миф', 'аллегория', 'анекдот', 'выдумка', 'посмешище', 'сказка']
        >>> SynonymSource.get_synonyms('путем')
        []

        :param word: russian word in initial form, lowercase
        :return: list of all synonyms, [] if where is no of them
        """
        return full_synonyms_list.get(word, [])

register_source(SynonymSource())
