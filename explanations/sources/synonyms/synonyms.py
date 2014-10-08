# noinspection PyProtectedMember
from explanations.sources.synonyms._synonyms_base import \
    initial_words, synonyms, noun_id
from explanations.sources.synonyms._synonyms_quality import \
    choose_best_synonyms
from explanations.sources_registry import register_source
from explanations.sources import ExplanationSource

__author__ = 'skird'

MAX_EXPLANATION_NUMBER_OF_SYNONYMS = 6

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
        return noun_id.keys()

    @classmethod
    def text_for_key(cls, key):
        s = choose_best_synonyms(key)
        if len(s) == 1:
            return 'синоним к слову ' + s[0]
        return 'синоним к словам ' + ', '.join(s)

register_source(SynonymSource())
