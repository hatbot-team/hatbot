__author__ = 'Алексей'

try:
    from . import _collocations_base
except SystemError:
    import _collocations_base

def explain_collocation(word):
    """
    Explains meaning of word with the help of collocation base.
    :param word: initial word to explain
    :return: List of explanations
    Example:
    >>> explain_collocation('учёт')
    ['Заполни пропуск и поставь слово в начальную форму. миграционного *пропуск*']
    >>> explain_collocation('язык')
    ['Заполни пропуск и поставь слово в начальную форму. русском *пропуск*']
    """
    if word in _collocations_base.collocation_explainable:
        explanations = _collocations_base.expl_collocation[word]
        result = ["Заполни пропуск и поставь слово в начальную форму: " + explanation
                    for explanation in explanations]
        return result
    else:
        return []

def get_all_explainable_words():
    """
    Gives all explainable words
    :return: Set with all explainable with collocation words
    """
    return _collocations_base.collocation_explainable

def get_all_explanations():
    """
    Gives all explanations
    :return: Dict if format string(word) -> list of strings(its explanations)
    Explanation in a dict is in a short form. You should also add phrase
    "Заполни пропуск и поставь слово в начальную форму: " in the beginning of any explanation
    """
    return _collocations_base.expl_collocation