__author__ = 'moskupols'

from .ExplanationSource import ExplanationSource

class GapExplanationSource(ExplanationSource):

    @classmethod
    def before_gap(cls, key):
        """
        Should return the part of explanation before the gap.

        :param key: key for restoring the explanation text
        :raise NotImplementedError: if not overridden
        """
        raise NotImplementedError

    @classmethod
    def after_gap(cls, key):
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
    def text_for_key(cls, key):
        return (cls.before_gap(key) + cls.gap_placeholder() + cls.after_gap(key)).strip()
