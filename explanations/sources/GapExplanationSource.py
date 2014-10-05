__author__ = 'moskupols'

from .ExplanationSource import ExplanationSource

class GapExplanationSource(ExplanationSource):

    def before_gap(self, key):
        """
        Should return the part of explanation before the gap.

        :param key: key for restoring the explanation text
        :raise NotImplementedError: if not overridden
        """
        raise NotImplementedError

    def after_gap(self, key):
        """
        Should return the part of explanation after the gap.

        :param key: key for restoring the explanation text
        :raise NotImplementedError: if not overridden
        """
        raise NotImplementedError

    def gap_placeholder(self):
        """
        :return: placeholder of the gap word.
        """
        return ' *пропуск* '

    def text_for_key(self, key):
        return (self.before_gap(key) + self.gap_placeholder() + self.after_gap(key)).strip()
