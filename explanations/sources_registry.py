__author__ = 'moskupols'

_source_for_name = dict()

def source_for_name(name):
    return _source_for_name[name]

def sources_registered():
    return _source_for_name.values()

def names_registered():
    return _source_for_name.keys()

def register_source(source):
    global _source_for_name
    if source.name in _source_for_name:
        raise KeyError("Source name '{}' redefinition".format(name))

    _source_for_name[source.name] = source
