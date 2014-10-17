__author__ = 'Oktosha'

import os
from sys import stderr
import codecs

COGNATES_PATH = \
    os.path.dirname(os.path.abspath(__file__)) + '/cognates.txt'


def init_cognates():
    try:
        cognates_file = codecs.open(COGNATES_PATH, "r", "utf-8")
    except FileNotFoundError:
        stderr.write('Cognates dictionary doesn\'t exist\n')
        return
    global cognates
    text = cognates_file.read()
    articles = text.split('\n\n')
    articles = [s.split('\n') for s in articles]
    articles = [[s[0].lower()] + sorted(set(s[1:])) for s in articles]
    for s in articles:
        for word in s[1:]:
            cognates[word] = []
    for s in articles:
        for word in s[1:]:
            cognates[word].append(s[0])


cognates = dict()
init_cognates()
