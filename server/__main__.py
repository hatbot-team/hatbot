__author__ = 'moskupols'

from .ExplanationServer import ExplanationServer
import cherrypy

cherrypy.quickstart(ExplanationServer())
