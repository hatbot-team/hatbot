#!/usr/bin/python3


def run_server(args):
    from server import run
    run(args.config)


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


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(description='Hatbot utilities')
    parser.add_argument('action',
                        choices=sorted(ACTIONS.keys()),
                        help='The action to be taken')
    parser.add_argument('--config',
                        help='path to the server config file')
    args = parser.parse_args()
    if args.action is not None:
        ACTIONS.get(args.action)(args)
