from . import _forms_base

def get_forms(initial):
	if initial in _forms_base.initial_to_forms:
		return list(_forms_base.initial_to_forms[initial])
	else:
		return None

def get_initial_forms(form):
	if form in _forms_base.form_to_initials:
		return list(_forms_base.form_to_initials[form])
	else:
		return None

