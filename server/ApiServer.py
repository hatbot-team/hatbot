import logging
import json

import cherrypy
import jsonschema

import explanator
from models import ScoreFeedback, get_database
from server.schemas import score_feedback_schema, chat_log_schema


__author__ = 'moskupols'
CHAT_LOGGER_NAME = 'api.chats'


def make_chat_logger():
    chat_logger = logging.getLogger(CHAT_LOGGER_NAME)
    chat_logger.setLevel(logging.INFO)

    ch = logging.FileHandler('chats.log', encoding='UTF-8')
    ch.setLevel(logging.INFO)

    formatter = logging.Formatter('%(asctime)s\n%(msg)s')

    ch.setFormatter(formatter)
    chat_logger.addHandler(ch)


make_chat_logger()


class ApiServer:
    @staticmethod
    def explanation_desc(e, asset: str):
        return {
            'id': e.key.encode(),
            'word': e.title,
            'text': e.text,
            'asset': asset
        }

    @staticmethod
    def unpack_asset_filter(joined):
        if joined is None:
            return None
        asset_filter = joined.split(',')
        for name in asset_filter:
            if not name in explanator.ALL_SOURCES_NAMES_SET:
                raise cherrypy.HTTPError(400, "Unknown asset '{}'".format(name))
        return asset_filter

    @staticmethod
    def get_explanation(word, joined_assets=None, method=explanator.explain):
        if word is None:
            raise cherrypy.HTTPError(400)
        e = method(word, ApiServer.unpack_asset_filter(joined_assets))
        if e is None or e == []:
            raise cherrypy.HTTPError(404, 'No explanation for word "{}"'.format(word))
        return e

    @staticmethod
    def receive_json(schema):
        data = cherrypy.request.json
        try:
            jsonschema.validate(data, schema)
        except jsonschema.ValidationError as err:
            raise cherrypy.HTTPError(400, err.message)
        return data

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def explain(self, word=None, assets=None):
        """
        Returns JSON described by explanation_schema
        """
        return self.explanation_desc(*self.get_explanation(word, assets))

    @cherrypy.expose
    @cherrypy.tools.json_out()
    def explain_list(self, word=None, assets=None):
        """
        Returns JSON described by explanation_list_schema
        """
        e_list = self.get_explanation(word, assets, method=explanator.explain_list)
        for i in range(len(e_list)):
            e_list[i] = self.explanation_desc(*e_list[i])
        return e_list

    @cherrypy.expose
    def explain_plain(self, word=None, assets=None):
        """
        Returns plain explanation text
        """
        return self.get_explanation(word, assets)[0].text

    @cherrypy.expose
    def random_word(self, selection_level=None, assets=None):
        if selection_level is not None and assets is not None:
            raise cherrypy.HTTPError(
                400, "Enhance your calm; you shan't specify both selection_level and assets")
        if selection_level is not None:
            selection_level = int(selection_level)
        elif assets is not None:
            assets = self.unpack_asset_filter(assets)
        else:
            selection_level = explanator.GOOD_WORDS_SELECTION
        return explanator.get_random_word(selection_level=selection_level, sources_names=assets)

    @cherrypy.tools.json_in(force=True)
    @cherrypy.expose
    def score(self):
        info = self.receive_json(score_feedback_schema)
        with get_database().transaction():
            ScoreFeedback.create(**info)

    @cherrypy.tools.json_in(force=True)
    @cherrypy.expose
    def chat_log(self):
        log = self.receive_json(chat_log_schema)
        logging.getLogger(CHAT_LOGGER_NAME).info(json.dumps(log))
