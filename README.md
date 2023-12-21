# Juoksukalenterisovellus

Juoksukalenterisovelluksella käyttäjät voivat suunnitella tulevia juoksuharjoituksiaan. 
Sovellus mahdollistaa suunniteltujen harjoitusten ja niistä tehtyjen yhteenvetojen tarkastelun. 

Toteutus on tehty Helsingin yliopiston ohjelmistotekniikan kurssilla syksyllä 2023. 

## Dokumentaatio

Linkki [käyttöohjeisiin](https://github.com/ah-pasila/ot-running-calendar/blob/master/dokumentaatio/kayttoohjeet.md)

Linkki [vaatimusmäärittelyyn](https://github.com/ah-pasila/ot-running-calendar/blob/master/dokumentaatio/vaatimusmaarittely.md)

Linkki [arkkitehtuuridokumentaatioon](https://github.com/ah-pasila/ot-running-calendar/blob/master/dokumentaatio/arkkitehtuuri.md)

Linkki [muutoslokiin](https://github.com/ah-pasila/ot-running-calendar/blob/master/dokumentaatio/changelog.md)

Linkki [työaikakirjanpitoon](https://github.com/ah-pasila/ot-running-calendar/blob/master/dokumentaatio/tyoaikakirjanpito.md)

## Sovelluksen asentaminen

- Huom. sovelluksen testauksessa käytetty Cubbli Linuxia ja Pythonin versiota 3.10.12, toimivuuutta muissa ympäristöissä ja muilla versioilla ei ole kokeiltu.

1. Lataa ohjelmakoodi komentorivillä 
```
git clone https://github.com/ah-pasila/ot-running-calendar/ 
```
tai lataama tuorein [release](https://github.com/ah-pasila/ot-running-calendar/releases) Githubista

2. Siirry ohjelmakansion juureen ja aja seuraava komento komentorivillä, jotta ohjelma saa käyttöön tarvittavat riippuvuudet: 
```
poetry install
```
(lisää tarvittaessa --no-root)

3. Alusta ohjelma ajamalla: 
```
poetry run invoke initialize
```
4. Käynnistä komentorivillä ajamalla noudetun kansion juuressa: 
```
poetry run invoke start
```