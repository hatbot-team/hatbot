import os
from statistics.statistics import Statistics, BlackList

__author__ = 'pershik'


def show_statistics():
    stat = Statistics()
    for explanation, (cnt_all, cnt_win) in stat.entries():
        print(explanation, cnt_all, cnt_win)


def show_blacklist():
    blacklist = BlackList()
    for explanation, cnt in blacklist.entries():
        print(explanation, cnt)


def show_all():
    print("Statistics:")
    show_statistics()

    print("\n\nBad explanations:")
    show_blacklist()

if __name__ == '__main__':
    show_all()
