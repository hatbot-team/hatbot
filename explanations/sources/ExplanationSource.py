__author__ = 'moskupols'

from ..explanation import Explanation

class ExplanationSource:

    @classmethod
    def explain(cls, word):
        return [Explanation(cls, key) for key in cls.keys_for(word)]

    @classmethod
    def represent_explanation(cls, key):
        return repr(key)

    @classmethod
    def keys_for(cls, word):
        raise NotImplementedError

    @classmethod
    def explainable_words(cls):
        raise NotImplementedError
