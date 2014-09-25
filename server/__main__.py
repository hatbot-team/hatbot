__author__ = 'moskupols'

from .ExplanationServer import ExplanationServer
import cherrypy

cherrypy.config.update("server/server.conf")
cherrypy.quickstart(ExplanationServer(), '/')
