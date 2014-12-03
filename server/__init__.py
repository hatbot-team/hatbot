from os import path

import cherrypy
from models import init_database, create_nonexistent_tables
from .ExplanationServer import ExplanationServer
from .StatisticsServer import StatisticsServer


__author__ = 'moskupols'


def run(db_url, conf=None):
    if conf is not None:
        cherrypy.config.update(conf)

    init_database(db_url)
    create_nonexistent_tables()

    static_conf = {
        '/': {
            'tools.staticdir.root': path.join(path.dirname(path.abspath(__file__)), 'static'),
            'tools.staticdir.on': True,
            'tools.staticdir.dir': '.',
            'tools.staticdir.index': 'index.html'
        }
    }

    cherrypy.tree.mount(ExplanationServer(), '/', static_conf)
    cherrypy.tree.mount(StatisticsServer(), '/statistics')
    cherrypy.engine.start()
    cherrypy.engine.block()
