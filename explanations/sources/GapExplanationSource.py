__author__ = 'moskupols'

from .ExplanationSource import ExplanationSource

class GapExplanationSource(ExplanationSource):

    @classmethod
    def gap_prefix(cls, key):
        raise NotImplementedError

    @classmethod
    def gap_suffix(cls, key):
        raise NotImplementedError

    @classmethod
    def gap_placeholder(cls):
        return ' *пропуск* '

    @classmethod
    def represent_explanation(cls, key):
        return cls.gap_prefix(key) + cls.gap_placeholder() + cls.gap_suffix(key)
