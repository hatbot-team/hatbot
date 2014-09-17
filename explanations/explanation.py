__author__ = 'moskupols'

# import enum
#
# SOURCES_LIST = ['collocations', 'phraseological']
# ExplanationSource = enum.Enum('ExplanationSource', ' '.join(SOURCES_LIST))

class Explanation:
    def __init__(self, source_class, key):
        self.source_class = source_class
        self.key = key

    def __repr__(self):
        return self.source_class.represent_explanation(self.key)
