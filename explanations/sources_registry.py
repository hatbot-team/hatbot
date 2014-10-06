__author__ = 'moskupols'

from explanations.sources import ExplanationSource

_source_for_name = dict()


def source_for_name(name)->ExplanationSource:
    ret = _source_for_name.get(name, None)
    if ret is None:
        raise KeyError("Unknown source {}".format(name))
    return ret


def sources_registered():
    return _source_for_name.values()


def names_registered():
    return _source_for_name.keys()


def register_source(source: ExplanationSource):
    global _source_for_name
    if source.name in _source_for_name:
        raise KeyError("Source name '{}' redefinition".format(source.name))

    _source_for_name[source.name] = source
