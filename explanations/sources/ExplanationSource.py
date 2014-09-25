__author__ = 'moskupols'

from explanations.explanation import Explanation


class ExplanationSource:

    @classmethod
    def explain(cls, word: str)->list:
        """
        Returns list of explanation.Explanation for the given word.

        >>> from explanations.sources import PhraseologicalSource
        >>> PhraseologicalSource.explain('голод')
        [*пропуск* не тетка]
        >>> PhraseologicalSource.explain('полка')
        [Класть зубы на *пропуск*, Положить зубы на *пропуск*]

        >>> from explanations.sources import CollocationsSource
        >>> CollocationsSource.explain('учёт')
        [миграционный *пропуск*]
        >>> CollocationsSource.explain('язык')
        [русский *пропуск*]

        >>> from explanations.sources import AntonymSource
        >>> AntonymSource.explain('свет')
        [антоним к словам тьма, мрак, темнота, тень]
        >>> AntonymSource.explain('альтруист')
        [антоним к слову эгоист]
        >>> AntonymSource.explain('диван')
        []

        :param word: russian noun in the initial form, in lowercase.
        :return: list of Explanation objects
        """
        return [Explanation(cls, key) for key in cls.keys_for(word)]

    @classmethod
    def represent_explanation(cls, key):
        """
        This method is used by explanation.Explanation to represent its information stored in key.
        If not overridden, returns repr(key).

        :param key: key generated by keys_for
        :return: string containing end user representation of the explanation
        """
        return repr(key)

    @classmethod
    def keys_for(cls, word: str):
        """
        This method is used by explain to initialize Explanations list. It should return a list of
        keys objects. Each of them has to be enough for represent_explanation to make the explanation text.

        :param word: the russian lowercase word to be explained
        :raise NotImplementedError: if not overridden by successors.
        """
        raise NotImplementedError

    @classmethod
    def explainable_words(cls):
        """
        Generates all words explainable using this source. Should be overridden by successors.
        :return: Iterable of explainable words
        :raise NotImplementedError: if not overridden by successors.
        """
        raise NotImplementedError
