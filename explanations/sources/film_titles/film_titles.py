from lang_utils.morphology.word_forms import get_valid_noun_initial_form

__author__ = 'makrusak'

from explanations.sources.film_titles._film_titles_base \
    import keys_dict, phrases_list
from explanations.sources.GapExplanationSource import GapExplanationSource
from explanations import sources_registry


class FilmTitlesSource(GapExplanationSource):

    def __init__(self):
        super().__init__('FilmTitlesSource')

    @classmethod
    def keys_for_word(cls, word):
        if word in keys_dict.keys():
            return [k for k in keys_dict[word]]
        else:
            return []

    @classmethod
    def word_for_key(cls, key):
        return get_valid_noun_initial_form(phrases_list[key[0]][key[1]])

    @classmethod
    def before_gap(cls, key):
        return 'Фильм: ' + ' '.join(phrases_list[key[0]][:key[1]])

    @classmethod
    def after_gap(cls, key):
        return ' '.join(phrases_list[key[0]][key[1] + 1:])

    @classmethod
    def explainable_words(cls):
        return keys_dict.keys()

sources_registry.register_source(FilmTitlesSource())
