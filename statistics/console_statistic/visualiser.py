import os
from statistics.statistics import Statistics, BlackList

__author__ = 'pershik'

STAT_PATH = os.path.dirname(os.path.abspath(__file__)) + "/statistic"
BLACK_PATH = os.path.dirname(os.path.abspath(__file__)) + "/bad_expl"


def show_statistics():
    stat = Statistics(STAT_PATH)
    for explanation, (cnt_all, cnt_win) in stat.entries():
        print(explanation, cnt_all, cnt_win)


def show_blacklist():
    blacklist = BlackList(BLACK_PATH)
    for explanation, cnt in blacklist.entries():
        print(explanation, cnt)


def show_all():
    print("Statistics:")
    show_statistics()

    print("\n\nBad explanations:")
    show_blacklist()

if __name__ == '__main__':
    show_all()
