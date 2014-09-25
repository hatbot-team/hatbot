__author__ = 'moskupols'

import cherrypy
import explanator
import pickle

PICKLE_PROTOCOL = 3

class ExplanationServer:
    @cherrypy.expose
    @cherrypy.tools.json_out()
    def explain(self, word=None):
        if word is None:
            raise cherrypy.HTTPError(400)
        e = explanator.explain(word)
        if e is None:
            raise cherrypy.HTTPError(400)
        return {'explanation': {
            'id_protocol': 'pickle' + str(PICKLE_PROTOCOL) + '+int-little',
            'id': int.from_bytes(pickle.dumps(e, PICKLE_PROTOCOL), 'little'),
            'text': repr(e)
        }}

    @cherrypy.expose
    def random_word(self):
        return explanator.get_random_word()

if __name__ == '__main__':
    cherrypy.quickstart(ExplanationServer())
