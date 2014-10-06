import cherrypy

from statistics import Statistics, BlackList
from utils import json_hooks as json
from explanations import Explanation


__author__ = 'moskupols'


class StatisticsServer:
    BLAME_RESULT = 'BLAME'
    ALLOWED_RESULTS = [BLAME_RESULT, Statistics.SUCCESS_RESULT, Statistics.FAIL_RESULT]

    def __init__(self):
        self.stat = Statistics()
        self.blacklist = BlackList()

        cherrypy.engine.subscribe('stop', self.stat.save)
        cherrypy.engine.subscribe('stop', self.blacklist.save)

    @cherrypy.tools.json_in(force=True)
    @cherrypy.expose
    def update(self):
        try:
            info = cherrypy.request.json

            try:
                result = info['result']
                explanation = json.unwrap(info['id'])
            except KeyError as e:
                raise cherrypy.HTTPError(400, 'KeyError: ' + str(e))

            if not isinstance(explanation, Explanation):
                raise cherrypy.HTTPError(400, 'The id should be an Explanation')
            if result not in self.ALLOWED_RESULTS:
                raise cherrypy.HTTPError(400,
                                         'Incorrect result, it should be a string from {}'
                                         .format(self.ALLOWED_RESULTS))

            if result == self.BLAME_RESULT:
                self.blacklist.blame(explanation)
            else:
                self.stat.update(explanation, result)

        except cherrypy.HTTPError as e:
            if e.code >= 500:
                raise e
            e.set_response()
            return e.args[-1]
