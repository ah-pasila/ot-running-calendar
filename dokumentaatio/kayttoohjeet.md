# Käyttöohjeet

## Sovelluksen asentaminen

1. Lataa ohjelmakoodi komentorivillä 
```
git clone https://github.com/ah-pasila/ot-running-calendar/ 
```
tai lataamalla tuorein kiinnitetty versio [release](https://github.com/ah-pasila/ot-running-calendar/releases) Githubista

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
Huom. sovelluksen testauksessa käytetty Cubbli Linuxia ja Pythonin versiota 3.10.12, toimivuuutta muissa ympäristöissä ja muilla versioilla ei ole kokeiltu.

## Kirjautuminen sovellukseen

Sovelluksen käyttöliittymä on tekstipohjainen eli toiminta perustuu käyttäjän näppäimistöltä antamiin syötetisiin. Sovelluksen käynnistyessä on mahdollista kirjautua sisään (1 ja enter) tai luoda uusi käyttäjätunnus (2 ja enter). Ohjelma sulkeutuu antamalla minkä tahansa muun merkin. 

Ensimmäistä kertaa käytettäessä käyttäjän on luotava käyttäjätunnus, salasana (vähintään 8 merkkiä) ja tallennettava sukupuoli ja ikä. Tämän jälkeen on tunnuksilla on mahdollista kirjautua sovellukseen.

## Sovelluksen aloitusvalikko

Sovellusvalikossa kirjautunut käyttäjä voi tallentaa juoksun antamalla syötteen 1, tulostaa tallennetut juoksut antamalla 2, tulostaa koosteen tallennetuista juoksuista antamalla 3 tai poistaa jonkin suunnitelluista juoksusta antamalla 4. Ohjelman voi sulkea antamalla minkä tahansa muun merkin. 

## Juoksun tallentaminen ja poisto

Juoksun tallentaminen alkaa, kun ohjelman päävalikossa annetaan syöte 1. Tulevasta juoksusta tallennetaan ajankohta muodossa YYYY-MM-DD, intensiteetti asteikolla 1-3 (syketason mukaan), kesto minuuteissa ja pituus kilometreissä sekä lisäksi juoksuharjoitukselle voi antaa vapaaehtoisen ja -muotoisen kuvauksen. Tallennuksen jälkeen palataan päävalikkoon, minkä jälkeen voi tallentaa uuden juoksun.

Valitsemalla päävalikosta 4 on mahdollista poistaa juoksu(t) annetulta päivämäärältä (muoto YYYY-MM-DD).

## Juoksujen tarkastelu

Tulevia juoksuja voi tarkastella antamalla syötteen 2. Valitsemalla 1 näytetään kaikki tuleviin ajankohtiin suunnitellut juoksut. Valitsemalla 2 on mahdollista valita haluttu tarkasteluajanjakso antamalla alku- ja loppupäivämäärät muodossa YYYY-MM-DD. Tarkastelun jälkeen palataan päävalikkoon.

## Juoksutilaston tarkastelu

Koostetta tulevista juoksusta voi tarkastella antamalla syötteen 3. Valitsemalla 1 näytetään kooste kaikista tuleviin ajankohtiin suunnitelluista juoksuista. Valitsemalla 2, on mahdollista valita haluttu tarkasteluajanjakso antamalla alku- ja loppupäivämäärät muodossa YYYY-MM-DD. Tarkastelun jälkeen palataan päävalikkoon.