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
    if word in _collocations_base.expl_collocation:
        return _collocations_base.expl_collocation[word]
    else:
        return []

def get_all_explanations():
    """
    Gives all explanations
    :return: Dict if format string(word) -> list of strings(its explanations)
    """
    return _collocations_base.expl_collocation