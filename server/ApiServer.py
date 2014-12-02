import cherrypy
import explanator
import datetime
from models import ScoreFeedback, get_database

__author__ = 'moskupols'


class ApiServer:
    @staticmethod
    def explanation_desc(e, asset: str):
        return {
            'id': e.key.encode(),
            'text': e.text,
            'asset': asset
        }

    @staticmethod
    def get_explanation(word, method=explanator.explain):
        if word is None:
            raise cherrypy.HTTPError(400)
        e = method(word)
        if e is None:
            raise cherrypy.HTTPError(400)
        return e

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def explain(self, word=None):
        return self.explanation_desc(*self.get_explanation(word))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def explain_list(self, word=None):
        e_list = self.get_explanation(word, method=explanator.explain_list)
        for i in range(len(e_list)):
            e_list[i] = self.explanation_desc(*e_list[i])
        return e_list

    @cherrypy.expose
    def explain_plain(self, word=None):
        return self.get_explanation(word)[0].text

    @cherrypy.expose
    def random_word(self):
        return explanator.get_random_word()

    @cherrypy.tools.json_in(force=True)
    @cherrypy.expose
    def score(self):
        try:
            info = cherrypy.request.json

            try:
                result = info['result']
                key = info['id']
            except KeyError as e:
                raise cherrypy.HTTPError(400, 'KeyError: ' + str(e))

            if result not in ScoreFeedback.verdict.choices:
                raise cherrypy.HTTPError(400,
                                         'Incorrect result, it should be a string from ' +
                                         str(ScoreFeedback.verdict.choices))

            with get_database().transaction():
                ScoreFeedback.create(
                    verdict=result,
                    timestamp=datetime.datetime.now(),
                    expl_key=key
                )

        except cherrypy.HTTPError as e:
            if e.code >= 500:
                raise e
            e.set_response()
            return e.args[-1]
