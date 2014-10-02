__author__ = 'moskupols'

_name_for_source = dict()
_source_for_name = dict()

def name_for_source(source)->str:
    return _name_for_source[source]

def source_for_name(name):
    return _source_for_name[name]

def sources_registered():
    return _name_for_source.keys()

def names_registered():
    return _source_for_name.keys()

def register_source(source, name):
    global _name_for_source, _source_for_name
    if name in _source_for_name:
        raise KeyError("Source name '{}' redefinition".format(name))
    if source in _name_for_source:
        raise KeyError("Explanation source re-enumeration ({}) is not supported yet".format(source))

    _name_for_source[source] = name
    _source_for_name[name] = source
