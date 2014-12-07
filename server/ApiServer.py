import logging
import cherrypy
import explanator
import jsonschema
from models import ScoreFeedback, get_database
from server.schemas import score_feedback_schema

__author__ = 'moskupols'


def make_chat_logger():
    chat_logger = logging.getLogger('api.chats')
    chat_logger.setLevel(logging.INFO)

    ch = logging.FileHandler('chats.log', encoding='UTF-8')
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s\n%(title)s\n%(text)s\n')

    ch.setFormatter(formatter)
    chat_logger.addHandler(ch)


make_chat_logger()


def store_chat_log(title, lines):
    logging.getLogger('api.chats').info('New chat', extra={'title': title, 'text': '\n'.join(lines)})


class ApiServer:
    @staticmethod
    def explanation_desc(e, asset: str):
        return {
            'id': e.key.encode(),
            'title': e.title,
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
        info = cherrypy.request.json

        try:
            jsonschema.validate(info, score_feedback_schema)
        except jsonschema.ValidationError as err:
            raise cherrypy.HTTPError(400, err.message)

        with get_database().transaction():
            ScoreFeedback.create(**info)

    @cherrypy.tools.json_in(force=True)
    @cherrypy.expose
    def chat_log(self):
        info = cherrypy.request.json

        try:
            title = info['title']
            lines = info['lines']
        except KeyError as e:
            raise cherrypy.HTTPError(400, 'KeyError: ' + str(e))

        if not isinstance(title, str) \
                or not isinstance(lines, list) \
                or any(not isinstance(s, str) or '\n' in s for s in lines):
            raise cherrypy.HTTPError(400, 'Incorrect typing')

        store_chat_log(title, lines)
