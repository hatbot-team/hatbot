__author__ = 'moskupols'

import cherrypy

from .ExplanationServer import ExplanationServer
from .StatisticsServer import StatisticsServer


def run(conf=None):
    if conf is not None:
        cherrypy.config.update(conf)
    cherrypy.tree.mount(ExplanationServer(), '')
    cherrypy.tree.mount(StatisticsServer(), '/statistics')
    cherrypy.engine.start()
    cherrypy.engine.block()
