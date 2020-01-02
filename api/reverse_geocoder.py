import falcon
import psycopg2
import os
import time

# Not for production use :)
attempts = 0

while attempts < 5:
    try:
        connection = psycopg2.connect('host=%(host)s password=%(password)s dbname=%(dbname)s user=%(username)s' % {
                    'host': os.getenv('DB_HOST', 'postgres'),
                    'dbname': os.getenv('DB_NAME', 'gisdemo'),
                    'username': os.getenv('DB_USERNAME', 'gisdemo'),
                    'password': os.getenv('DB_PASSWORD', 'gisdemo'),
                })
        break
    except:
        print("Connection to postgres failed. Attempting again in 5 seconds")
        time.sleep(5)
        attempts += 1

if not connection:
    print("Failed to connect to postgres!")


class LookupResource:
    def on_get(self, req, resp):
        with connection.cursor() as cursor:
            x = int(req.params['x'])
            y = int(req.params['y'])
            query = """SELECT distinct(street_name) FROM street WHERE ST_DWithin(geometry,
            ST_SetSRID(ST_Point(%(X)d, %(Y)d), 3067), 100)""" % {'X': x, 'Y': y}
            cursor.execute(query)
            results = []
            for result in cursor.fetchall():
                results.append(result[0])

            resp.media = list(results)


print("""
db       .d88b.   .d88b.  db   dD db    db d8888b.
88      .8P  Y8. .8P  Y8. 88 ,8P' 88    88 88  `8D
88      88    88 88    88 88,8P   88    88 88oodD'
88      88    88 88    88 88`8b   88    88 88~~~
88booo. `8b  d8' `8b  d8' 88 `88. 88b  d88 88
Y88888P  `Y88P'   `Y88P'  YP   YD ~Y8888P' 88
""")
print("Waiting for connections.")

api = falcon.API()
api.add_route('/lookup', LookupResource())
