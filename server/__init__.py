__author__ = 'moskupols'

from .ExplanationServer import ExplanationServer
from .StatisticsServer import StatisticsServer
import cherrypy

cherrypy.config.update("server/server.conf")
cherrypy.tree.mount(ExplanationServer(), '')
cherrypy.tree.mount(StatisticsServer(), '/statistics')

def run():
    cherrypy.engine.start()
    cherrypy.engine.block()
