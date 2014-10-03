__author__ = 'moskupols'

import cherrypy
import explanator


class ExplanationServer:

    @cherrypy.expose
    def index(self):
        return "wake up neo"

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def explain(self, word=None):
        if word is None:
            raise cherrypy.HTTPError(400)
        e = explanator.explain(word)
        if e is None:
            raise cherrypy.HTTPError(400)
        return {
            'explanation': {
                'id': e.json_serializable(),
                'text': e.text
            }
        }

    @cherrypy.expose
    def explain_plain(self, word=None):
        if word is None:
            raise cherrypy.HTTPError(400)
        e = explanator.explain(word)
        if e is None:
            raise cherrypy.HTTPError(400)
        return e.text

    @cherrypy.expose
    def random_word(self):
        return explanator.get_random_word()
