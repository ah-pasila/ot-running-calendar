# Testausdokumentti

## Yksikkö- ja integraatiotestaus

Testeissä käytettiin unittestiä. Testausta tehtiin luokissa [TestRunCalendarService](https://github.com/ah-pasila/ot-running-calendar/blob/master/src/tests/run_calendar_service_test.py), [TestRunRepository](https://github.com/ah-pasila/ot-running-calendar/blob/master/src/tests/run_repository_test.py) ja [TestUserRepository](https://github.com/ah-pasila/ot-running-calendar/blob/master/src/tests/user_repository_test.py). Ne vastaavat toteutuksen vastaavasti nimettyjä luokkia. 

Alla testikattavuusraportti.

![Coverage report](https://github.com/ah-pasila/ot-running-calendar/blob/master/dokumentaatio/kuvat/image.png)

## Järjestelmätestaus

Järjestelmätestaus on suoritettu manuaalisesti viimeisimmälle releasille [käyttöohjeiden](https://github.com/ah-pasila/ot-running-calendar/blob/master/dokumentaatio/kayttoohjeet.md) mukaan. Testauksessa on toteutettu ohjeen mukaisia tavanomaisia toimintoja eli käyttäjän luonti, sisäänkirjautuminen, juoksun tietojen tallennus ja poisto sekä tarkastelu eri rajauksilla ja sovelluksesta poistuminen.

## Puutteita 

Testaus alkoi liian myöhäisessä vaiheessa sovelluskehitystä ja jäi melko puutteelliseksi, erityisesti integraatiotestauksen osalta, jota tarvittiin RunCalendarService-luokan osalta. 

Testauksen kannalta paljastui ongelmalliseksi ratkaisuksi jättää iso osa virhekäsittelyistä (syötteeseen liittyen) käyttöliittymään, jota ei testattu.

Myös ui-puolelle jäi validointipuutteita, ainakin yksi havaittu on se, että tyhjän käyttäjänimen tallentaminen onnistuu (tosin vain kertaluontoisesti).

Testausta varten ei muodosteta testitietokantaa ei muodosteta, mikä olisi ollut hyvä. Ennen sovelluksen käyttöä tuotannossa on siis erittäin tärkeää ohjeiden mukaisesti alustaa tietokanta. Tämän tekemättä jättämisestä ei kuitenkaan sinänsä varoiteta. 

Syötteen pituudelle on joissakin tapauksissa asetettu alaraja, mutta ei ylärajaa eli todennäköisesti antamalla hyvin pitkiä syötteitä voi aiheuttaa ongelmia sovelluksen toiminnalle, mutta tätä ei kuitenkaan testattu.

Lisäksi testaukselle ongelmia aiheutti tapa, miten säilytettiin tietoa kirjautuneesta käyttäjästä - tämä olisi pitänyt toteuttaa joko eri tavoin tai muistaa kirjata testeissä käytetty käyttäjä sisään.