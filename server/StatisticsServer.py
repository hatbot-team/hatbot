import cherrypy
import datetime
from models import ScoreFeedback, get_database


__author__ = 'moskupols'


class StatisticsServer:
    @cherrypy.tools.json_in(force=True)
    @cherrypy.expose
    def update(self):
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
