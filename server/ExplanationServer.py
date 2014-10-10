from utils import json_hooks

__author__ = 'moskupols'

import cherrypy
import explanator


class ExplanationServer:

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def explain(self, word=None):
        if word is None:
            raise cherrypy.HTTPError(400)
        e = explanator.explain(word)
        if e is None:
            raise cherrypy.HTTPError(400)
        return {
            'id': json_hooks.serializable(e),
            'text': e.text()
        }

    @cherrypy.expose
    def explain_plain(self, word=None):
        if word is None:
            raise cherrypy.HTTPError(400)
        e = explanator.explain(word)
        if e is None:
            raise cherrypy.HTTPError(400)
        return e.text()

    @cherrypy.expose
    def random_word(self):
        return explanator.get_random_word()
