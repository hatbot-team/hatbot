from copy import copy
import itertools
import random

__author__ = 'moskupols'


class Explanator:
    def __init__(self, sources_by_tag: dict):
        self._sources_by_tag = copy(sources_by_tag)

        # create index by name
        self._sources_by_name = \
            {source.name: source for source in itertools.chain(*self._sources_by_tag.values())}
        # create additional tag consisting of all sources
        self._sources_by_tag['all'] = list(self._sources_by_name.values())

        # some additional indexes, could be replaced by properties, getters or other views
        self._names_by_tag = \
            {l: [s.name for s in sources] for l, sources in self._sources_by_tag.items()}
        self._word_list_by_name = \
            {name: list(source.explainable_words()) for name, source in self._sources_by_name.items()}
        self._all_names = self._sources_by_name.keys()
        self._all_words_set = frozenset(itertools.chain(*self._word_list_by_name.values()))

    def _sourceish_to_names(self, sourceish):
        if sourceish is None:
            # all sources
            return list(self._all_names)
        else:
            if isinstance(sourceish, str):
                # one source
                sourceish = [sourceish]
            # list of names
            result = []
            for n in sourceish:
                if n in self._all_names:
                    result.append(n)
                else:
                    assert n in self._names_by_tag
                    result.extend(self._names_by_tag[n])
            return list(set(result))

    def _sourceish_to_sources(self, sourceish):
        return list(map(self._sources_by_name.get, self._sourceish_to_names(sourceish)))

    def get_explainable_words(self, sourceish=None):
        """
        Returns an iterable of all words for which we have any explanation.

        :return: iterable
        """
        return itertools.chain(*map(self._word_list_by_name.get, self._sourceish_to_names(sourceish)))

    def get_random_word(self, sourceish=None):
        source_names = self._sourceish_to_names(sourceish)
        assert len(source_names)

        # we want to pick a uniformly random element from several lists,
        # but we wouldn't like to join them, as they are long
        lists = list(map(self._word_list_by_name.get, source_names))
        total = sum(map(len, lists))
        rand = random.randrange(total)
        upto = 0
        for word_list in lists:
            upto += len(word_list)
            if rand < upto:
                return word_list[rand - upto]  # yep, negative indexation
        assert False, 'Shouldn\'t get here'

    def explain_list(self, word, sourceish=None):
        """
        Returns list of tuples (Explanations, asset_name)
        """
        if word not in self._all_words_set:
            return []
        sources = self._sourceish_to_sources(sourceish)
        res = list()
        for s in sources:
            res.extend(zip(s.explain(word), itertools.repeat(s.name)))
        random.shuffle(res)
        return res

    def explain(self, word, sourceish=None):
        """
        Returns a tuple (Explanation, asset_name)

        :param word: a russian noun in lowercase
        :return: the explanation
        """
        explanations = self.explain_list(word, sourceish)
        return explanations[0] if len(explanations) else None

    @property
    def source_names(self):
        return self._all_names

    @property
    def tags(self):
        return frozenset(self._names_by_tag.keys())
