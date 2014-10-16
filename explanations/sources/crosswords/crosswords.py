__author__ = 'Keks'

from explanations.sources.ExplanationSource import ExplanationSource
from explanations import sources_registry

from explanations.sources.crosswords._crosswords_base \
    import keys_list, crosswords_dict

class CrosswordSource(ExplanationSource):
    def __init__(self):
        super().__init__('CrosswordSource')

    @classmethod
    def keys_for_word(cls, word):
        if word not in keys_list.keys():
            return []
        else:
            return [def_key for def_key in keys_list[word]]


    @classmethod
    def word_for_key(cls, key) -> str:
        return crosswords_dict[key][0]

    @classmethod
    def text_for_key(cls, key):
        return crosswords_dict[key][1]

    @classmethod
    def explainable_words(cls):
        return keys_list.keys()

sources_registry.register_source(CrosswordSource())