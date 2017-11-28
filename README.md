# Taiste GIS-workshop

- Lataa ja asenna QGIS http://qgis.org/
- Lataa ja asenna PostgreSQL-tietokanta ja PostGIS-laajennos (http://postgis.net/install/)
- Lataa http://kartat.kapsi.fi/files/maastotietokanta/tiesto_osoitteilla/etrs89/shp/L33.shp.zip
- Lataa ja asenna myös Python ja `pip-requirements.txt` -tiedoston sisältämät kirjastot
  komennolla `pip install -r pip-requirements.txt`

Workshopin tarkoituksena on tehdä kevyt tutkimusretki Geographic Information Systemin
(GIS) eli vapaasti suomennettuna paikkatietodatan maailmaan.

Käytämme lähteenämme Maanmittauslaitoksen julkaisemaa vektoripohjaista dataa, tutkitaan
mitä se on syönyt. Jos ehdimme, toteutetaan sen pohjalle hyvin kevyt kääneteinen
geokoodaus, jonka avulla syöttämällä koordinaatin saa palautteena lähimmät kadunnimet.
