__author__ = 'moskupols'

try:
    from .morph import morph
except SystemError:
    from morph import morph


# def get_forms(initial):
#     """
#     Get all possible forms of a given word in initial form.
#
#     >>> get_forms('мама')
#     ['мам', 'мама', 'мамам', 'мамами', 'мамах', 'маме', 'мамой', 'мамою', 'маму', 'мамы']
#     >>> get_forms('мыла')
#
#     :param initial: a russian word in its initial form, in lower case
#     :return: a list of forms if the word is found in the dictionary, None otherwise
#     """
#     parsed = morph.parse(initial)
#     ans = []
#     for p in parsed:
#         ans.extend(p.inflect(...))


def get_initial_forms(form, part_filter=None):
    """
    Gets all possible initial forms (there are several of them sometimes) of a given word.
    Optional argument part_filter allows to prune unnecessary ambiguity with part of speech.

    >>> get_initial_forms('Дядя')
    ['дядя']
    >>> get_initial_forms('самых')
    ['самый']
    >>> get_initial_forms('честных')
    ['честной', 'честный']
    >>> get_initial_forms('правил')
    ['правило', 'править']
    >>> get_initial_forms('правил', 'NOUN')
    ['правило']
    >>> get_initial_forms('правил', ['VERB'])
    ['править']

    :param form: a russian word
    :param part_filter: something that supports `in' operator: str, list, set etc. If it is a container,
    it should contain only Part-of-speech names according to pymorphy2 enumerations
    :return: a list of possible initial forms of the given word in lowercase.
    It's guaranteed that there are no repetitions.
    Variants are generated in the order of descending certainty.
    """
    met = set()
    ret = []
    for p in morph.parse(form):
        if p.score < .1:
            continue
        if part_filter is None or p.tag.POS in part_filter:
            norm = p.normal_form
            if norm not in met:
                ret.append(norm)
                met.add(norm)
    return ret
