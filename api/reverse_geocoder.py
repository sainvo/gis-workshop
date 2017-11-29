import falcon
import psycopg2
import os

connection = psycopg2.connect('dbname=%(dbname)s user=%(username)s' % {
    'dbname': os.getenv('DB_NAME', os.getenv('USER')),
    'username': os.getenv('DB_USERNAME', os.getenv('USER'))
})


class LookupResource:
    def on_get(self, req, resp):
        with connection.cursor() as cursor:
            x = int(req.params['x'])
            y = int(req.params['y'])
            query = """SELECT street_name FROM street WHERE ST_DWithin(geometry,
            ST_SetSRID(ST_Point(%(X)d, %(Y)d), 3067), 100)""" % {'X': x, 'Y': y}
            cursor.execute(query)
            results = set()
            for result in cursor.fetchall():
                results.add(result[0].decode('utf-8'))

            resp.media = list(results)

api = falcon.API()
api.add_route('/lookup', LookupResource())
