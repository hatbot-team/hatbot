#!/usr/bin/python3


def run_server(_):
    from server import run
    run()


def play(_):
    from statistics.console_statistic.statistic_builder import interact
    interact()


def stats(_):
    from statistics.console_statistic.visualiser import show_all
    show_all()


ACTIONS = {
    'server': run_server,
    'play': play,
    'stats': stats
}


def main(argv):
    if len(argv) < 2 or argv[1] not in ACTIONS:
        print('usage: {} {}'.format(argv[0], '|'.join(list(ACTIONS.keys()))))
        return
    ACTIONS.get(argv[1])(argv)

if __name__ == '__main__':
    import sys
    main(sys.argv)
