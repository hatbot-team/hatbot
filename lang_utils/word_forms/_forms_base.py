__author__ = 'moskupols'

import os

FORMS_BASE_PATH = os.path.dirname(os.path.abspath(__file__)) + '/word_forms.txt'


def init_base():
    forms_base = open(FORMS_BASE_PATH)

    global initial_to_forms, form_to_initials

    for line in forms_base:
        initial = None
        for w in line.strip().split():
            if initial is None:
                initial = w
                initial_to_forms[initial] = set()
                continue
            if w not in form_to_initials:
                form_to_initials[w] = set()
            initial_to_forms[initial].add(w)
            form_to_initials[w].add(initial)

    forms_base.close()

    for k in initial_to_forms.keys():
        initial_to_forms[k] = list(sorted(initial_to_forms[k]))
    for k in form_to_initials.keys():
        form_to_initials[k] = list(sorted(form_to_initials[k]))

initial_to_forms = dict()
form_to_initials = dict()

init_base()
