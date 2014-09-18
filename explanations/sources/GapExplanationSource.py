__author__ = 'moskupols'

from .ExplanationSource import ExplanationSource

class GapExplanationSource(ExplanationSource):

    @classmethod
    def gap_prefix(cls, key):
        """
        Should return the part of explanation before the gap.

        :param key: key for restoring the explanation text
        :raise NotImplementedError: if not overridden
        """
        raise NotImplementedError

    @classmethod
    def gap_suffix(cls, key):
        """
        Should return the part of explanation after the gap.

        :param key: key for restoring the explanation text
        :raise NotImplementedError: if not overridden
        """
        raise NotImplementedError

    @classmethod
    def gap_placeholder(cls):
        """
        :return: placeholder of the gap word.
        """
        return ' *пропуск* '

    @classmethod
    def represent_explanation(cls, key):
        return (cls.gap_prefix(key) + cls.gap_placeholder() + cls.gap_suffix(key)).strip()
