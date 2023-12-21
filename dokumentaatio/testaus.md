# Testausdokumentti

## Yksikkö- ja integraatiotestaus

## Järjestelmätestaus

Järjestelmätestaus on suoritettu viimeisimmälle releasille [käyttöohjeiden](https://github.com/ah-pasila/ot-running-calendar/blob/master/dokumentaatio/kayttoohjeet.md) mukaan. Testauksessa on toteutettu ohjeen mukaisia tavanomaisia toimintoja eli käyttäjän luonti, sisäänkirjautuminen, juoksun tietojen tallennus ja poisto sekä tarkastelu eri rajauksilla ja sovelluksesta poistuminen.

## Puutteita 

Testaus alkoi liian myöhäisessä vaiheessa sovelluskehitystä ja jäi melko puutteelliseksi, erityisesti integraatiotestauksen osalta. 

Testauksen kannalta paljastui ongelmalliseksi ratkaisuksi, jättää iso osa virhekäsittelyistä (syötteeseen liittyen) käyttöliittymään, jota ei testattu.

Testausta varten ei muodosteta testitietokantaa ei muodosteta, mikä olisi ollut hyvä. Ennen sovelluksen käyttöä tuotannossa on siis erittäin tärkeää ohjeiden mukaisesti alustaa tietokanta. Tämän tekemättä jättämisestä ei kuitenkaan sinänsä varoiteta. 

Syötteen pituudelle on joissakin tapauksissa asetettu alaraja, mutta ei ylärajaa eli todennäköisesti antamalla hyvin pitkiä syötteitä voi aiheuttaa ongelmia sovelluksen toiminnalle, mutta tätä ei kuitenkaan testattu.