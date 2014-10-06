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


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='''Hatbot utilities. See hatbot.py utility -h for info on utility params.''')
    subparsers = parser.add_subparsers()

    server_parser = subparsers.add_parser('server',
                                          help='''Run server.
             Note that the server restarts automatically every time some source file is changed.
             Even more, at 93.175.... it is checked every 10m and restarted if found not running.
        ''')
    server_parser.add_argument('--config',
                               help='path to the server config file')
    server_parser.set_defaults(func=run_server)

    play_parser = subparsers.add_parser('play', help='run statistics gathering utility')
    play_parser.set_defaults(func=play)

    stats_parser = subparsers.add_parser('stats', help='output statistics')
    stats_parser.set_defaults(func=stats)

    args = parser.parse_args()
    args.func(args)
