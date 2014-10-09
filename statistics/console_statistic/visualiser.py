from statistics.statistics import Statistics, BlackList

__author__ = 'pershik'


def print_entries(stat):
    for explanation, info in stat.entries():
        if explanation.is_reproducible():
            print(info, explanation.word(), ':=', explanation, '---', repr(explanation))
        else:
            print(info, '<not reproducible>', '---', repr(explanation))
    print()
    print('Total {} entries'.format(len(stat.entries())))


def show_statistics():
    print_entries(Statistics())


def show_blacklist():
    print_entries(BlackList())


def show_all():
    print("Statistics:")
    show_statistics()

    print("\n\nBad explanations:")
    show_blacklist()

if __name__ == '__main__':
    show_all()
