Continuous Integration / Continuous Deployment on olennainen osa nykyaikaista ohjelmistokehitystä. Kyse on oikeastaan laaduntarkkailusta ja varmistamisesta, siitä että virheet eivät päädy tuotantoon asti.
Keskeiset ci-putken osat ovat: linttaus, testaus ja buildaaminen.

Eri kielille on luonnollisesti omat työkalunsa: esim. JavaScriptille yleisiä linttaustyökaluja ovat ESLint ja JSLint, kun taas testaamiseen voi käyttää työkaluja kuten Jest tai Mocha tai cypress e2e testejä. 
Buildaamiseen suosittuja työkaluja ovat esimerkiksi Webpack tai Babel. Versionhallintaan mm. npm.

Jenkins ja GitHub Actions ovat tunnettuja CI-järjestelmävaihtoehtoja, mutta on olemassa myös muita vaihtoehtoja, kuten CircleCI, Travis CI, GitLab CI/CD ja Bitbucket Pipelines.

Ratkaistessa, olisiko Ci-putki parempi itsehallinnoidussa vai pilvipohjaisessa ympäristössä, riippuu tarpeesta. Edellisen etuna on täysi hallinta ja hallinnollinen vapaus, kun kehittäjät voivat mukauttaa 
ympäristön tarpeidensa mukaan ja pitää sen esim. sisäverkossa, mikä voi parantaa tietoturvaa. 
Lisäksi itsehallinnoidussa ympäristö voi (ehkä?) olla taloudellisesti kannattava vaihtoehto pitkällä aikavälillä, jos ohjelmistokehitystarpeet ovat jatkuvia.

Toisaalta pilvipohjainen ympäristö tarjoaa skaalautuvuutta ja usein myös helppokäyttöisyyttä. Pilvipalvelut tarjoavat usein valmiita ratkaisuja Ci-putken käyttöön, mikä säästää aikaa ja vaivaa = rahaa!
Lisäksi pilvipohjainen ympäristö voi tarjota enemmän joustavuutta työskennellä etänä.

Eli päätöstä tehdessä tarvitaan tietoa mm. budjetista, turvallisuusvaatimuksista, tiimen osaamisesta ja resursseista jne. Ja tietenkin myös skaalautuvuuden tarpeet on olennainen kysymys, joka kannattaa ottaa jo aikaisessa 
vaiheessa huomioon.

Jos organisaatiolla on rajoitettu budjetti ja erityisiä turvallisuusvaatimuksia, itse-isännöity ympäristö voi olla parempi vaihtoehto. 
Jos taas joustavuus ja nopea käyttöönotto ovat ensisijaisia, pilvipohjainen ympäristö voi olla parempi.
