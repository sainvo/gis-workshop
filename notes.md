GIS = geographic information system
stores data and works as an API

PostGIS: based on Postgresql database
QGIS = open source tool

* using local coordinate system nationally
* WG8 for a compromise compiled version of the whole world based on teh local coordinate versions


_____
project- parameters : FIN
layer- add layer -> L-33 layer


docker-compose exec postgres psql -U gisdemo -h localhost gisdemo
pw = gisdemo

street is the primary key

cat "file path" | docker-compose exec -T postgres bash-c 'PGPASSWORD=gisdemo spql -U gisdemo - localhost'