# Taiste GIS-workshop

- Lataa ja asenna Docker ja Docker Compose
  (*Windows*: https://docs.docker.com/docker-for-windows/install/
   *OS X*: https://docs.docker.com/docker-for-mac/install/)
- Lataa ja asenna QGIS http://qgis.org/
- Lataa http://kartat.kapsi.fi/files/maastotietokanta/tiesto_osoitteilla/etrs89/shp/L33.shp.zip

Workshopin tarkoituksena on tehdä kevyt tutkimusretki Geographic Information Systemin
(GIS) eli vapaasti suomennettuna paikkatietodatan maailmaan.

Käytämme lähteenämme Maanmittauslaitoksen julkaisemaa vektoripohjaista dataa, tutkitaan
mitä se on syönyt. Jos ehdimme, toteutetaan sen pohjalle hyvin kevyt kääneteinen
geokoodaus, jonka avulla syöttämällä koordinaatin saa palautteena lähimmät kadunnimet.

Käynnistä ympäristö komennolla

```docker-compose up```
