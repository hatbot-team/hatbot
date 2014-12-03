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
        description='''Hatbot utilities. See hatbot.py utility -h for info on utility params.''',
        formatter_class=argparse.RawTextHelpFormatter)
    subparsers = parser.add_subparsers()

    server_parser = subparsers.add_parser('server',
                                          help='Run server. Localhost (127.0.0.1:8080) by default.\n'
                                               'Note that the server restarts automatically every time some source '
                                               'file is changed.\n',
                                          formatter_class=argparse.RawTextHelpFormatter)
    server_parser.add_argument('--config',
                               help="Path to cherrypy config file. \n"
                                    "See https://cherrypy.readthedocs.org/en/latest/basics.html#configuring\n"
                                    "\n"
                                    "Also you can specify database url somehow like this:\n"
                                    "[db]\n"
                                    "url = 'sqlite:///some.db'\n"
                                    "# or\n"
                                    "url = 'postgresql://user:password@host:5432/database'\n"
                                    "\n"
                                    "It's worth noting though that you'll need to install psycopg2 package\n"
                                    "in order to use postgresql with hatbot.")
    server_parser.set_defaults(func=run_server)

    play_parser = subparsers.add_parser('play', help='Run statistics gathering utility')
    play_parser.set_defaults(func=play)

    stats_parser = subparsers.add_parser('stats', help='Output statistics')
    stats_parser.set_defaults(func=stats)

    args = parser.parse_args()
    if hasattr(args, 'func'):
        args.func(args)
    else:
        parser.print_usage()
