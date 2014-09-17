__author__ = 'Алексей'

try:
    from . import _phraseological_base
except SystemError:
    import _phraseological_base

from explanations.sources.ExplanationSource import ExplanationSource

class PhraseologicalSource(ExplanationSource):

    @classmethod
    def keys_for(cls, word):
        """
        Explains meaning of the word with the help of phraseologism base
        :param word: word to explain
        :return: list of explanations
        Example:
        >>> PhraseologicalSource.keys_for('голод')
        ['*пропуск* не тетка ']
        >>> PhraseologicalSource.keys_for('полка')
        ['Класть зубы на *пропуск* ', 'Положить зубы на *пропуск* ']
        """
        if word in _phraseological_base.phraseological_explainable:
            return [e for e in _phraseological_base.expl_phraseological[word]]
        else:
            return []


    @classmethod
    def represent_explanation(cls, key):
        return "Заполни пропуск и поставь слово в начальную форму: " + key


    @classmethod
    def explainable_words(cls):
        """
        Gives all explainable words
        :return: Set of explainable words with the help of phraseologism
        """
        return _phraseological_base.phraseological_explainable
