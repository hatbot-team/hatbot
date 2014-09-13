import os

FORMS_BASE_PATH = \
	os.path.dirname(os.path.abspath(__file__)) + '/word_forms.txt'

def init_base():
	try:
		forms_base = open(FORMS_BASE_PATH)
	except:
		pass

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

initial_to_forms = dict()
form_to_initials = dict()

init_base()

