try:
    from . import _forms_base
except SystemError:
    import _forms_base


def get_forms(initial):
    """
    Get all possible forms of a given word in initial form.

    >>> get_forms('мама')
    ['мам', 'мама', 'мамам', 'мамами', 'мамах', 'маме', 'мамой', 'мамою', 'маму', 'мамы']
    >>> get_forms('мыла')

    :param initial: a russian word in its initial form, in lower case
    :return: a list of forms if the word is found in the dictionary, Null otherwise
    """
    if initial in _forms_base.initial_to_forms:
        return list(_forms_base.initial_to_forms[initial])
    else:
        return None


def get_initial_forms(form):
    """
    Get all possible initial forms (there are several of them sometimes) of a given word.

    >>> get_initial_forms('Мама')
    >>> get_initial_forms('мыла')
    ['мыло', 'мыть']
    >>> get_initial_forms('раму')
    ['рама']

    :param form: a russian word in lower case
    :return: a list of possible initial forms if the word is found in the dictionary, Null otherwise
    """
    if form in _forms_base.form_to_initials:
        return list(_forms_base.form_to_initials[form])
    else:
        return None
