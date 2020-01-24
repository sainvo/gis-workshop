# Run in QGIS to generate SQL

from io import StringIO
from binascii import hexlify
from qgis.utils import iface

turku = iface.activeLayer()

clause = StringIO()
clause.write("""BEGIN;\n
INSERT INTO street (street_name, geometry) VALUES
""")

rows = []
for f in turku.getFeatures():
    if f['TEKSTI']:
        rows.append("\t('%s', ST_GeomFromWKB(decode('%s', 'hex'), 3067))\n" % (f['TEKSTI'].replace("'", "''"), hexlify(f.geometry().asWkb()).upper()))

clause.write(',\n'.join(rows))
clause.write("; COMMIT")

with open('/tmp/addresses.sql', 'w', encoding='utf-8') as f:
    f.write(clause.getvalue())
