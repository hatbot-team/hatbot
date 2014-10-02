__author__ = 'moskupols'

from . import sources_registry


class Explanation:
    def __init__(self, source, key):
        if not source in sources_registry.sources_registered() and\
           not source in sources_registry.names_registered():
            raise KeyError("Unknown source {}, register it with sources_registry".format(source))
        if not isinstance(source, str):
            source = sources_registry.name_for_source(source)

        self.source_name = source
        self.key = key

    def __str__(self):
        return self.text

    @property
    def text(self)->str:
        return sources_registry.source_for_name(self.source_name).text_for_key(self.key)
