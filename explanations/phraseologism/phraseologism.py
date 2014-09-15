__author__ = 'Алексей'

try:
    from . import _phraseologism_base
except SystemError:
    import _phraseologism_base

def explain_phraseologism(word):
    """
    Explains meaning of the word with the help of phraseologism base
    :param word: word to explain
    :return: list of explanations
    Example:
    >>> explain_phraseologism('голод')
    ['Заполни пропуск и поставь слово в начальную форму: *пропуск* не тетка ']
    >>> explain_phraseologism('полка')
    ['Заполни пропуск и поставь слово в начальную форму: Класть зубы на *пропуск* ',
     'Заполни пропуск и поставь слово в начальную форму: Положить зубы на *пропуск* ']
    """
    if word in _phraseologism_base.phraseologism_explainable:
        explanations = _phraseologism_base.expl_phraseologism[word]
        result = ["Заполни пропуск и поставь слово в начальную форму: " + explanation
                    for explanation in explanations]
        return result
    else:
        return []


def get_all_explanations():
    """
    Gives all explanations
    :return: Dict if format string(word) -> list of strings(its explanations)
    Explanation in a dict is in a short form. You should also add phrase
    "Заполни пропуск и поставь слово в начальную форму: " in the beginning of any explanation
    """
    return _phraseologism_base.expl_phraseologism


def get_all_explainable_words():
    """
    Gives all explainable words
    :return: Set of explainable words with the help of phraseologism
    """
    return _phraseologism_base.phraseologism_explainable