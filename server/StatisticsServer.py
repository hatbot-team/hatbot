from explanations.explanation import Explanation

__author__ = 'moskupols'

import cherrypy
from statistics import Statistics, BlackList


class StatisticsServer:
    def __init__(self):
        self.stat = Statistics()
        self.blacklist = BlackList()

        cherrypy.engine.subscribe('stop', self.stat.save)
        cherrypy.engine.subscribe('stop', self.blacklist.save)

    @cherrypy.tools.json_in(force=True)
    @cherrypy.expose
    def update(self):
        info = cherrypy.request.json

        result = info['result']
        explanation = Explanation.decode_json(info['id'])

        if result == 'BLAME':
            self.blacklist.blame(explanation)
        else:
            self.stat.update(explanation, result)
