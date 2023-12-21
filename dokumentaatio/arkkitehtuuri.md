# Arkkitehtuuridokumentaatio

## Rakenne

Sovelluskoodi on kerrosarkkitehtuuriajattelua noudattaen jaettu pakkauksiin ui (käyttöliittymä), services (sovellustoiminnot), entities (luokat) ja repositories (tallennus- ja lukuratkaisut).

Käyttöliittymä luo instanssin sovelluksesta, joka puolestaan kutsuu varsinaisia entities-luokkia ja repositories-luokkia, jotka vastaavat tiedon tallennuksesta tietokantaan ja noutamisesta. 

## Käyttöliittymä - UI

Sovelluksessa on tekstipohjainen käyttöliittymä, joka on yhdessä luokassa [Ui](https://github.com/ah-pasila/ot-running-calendar/blob/master/src/ui/ui.py). Sovellus- ja käyttöliittymätoiminnot on pyritty pitämään erillään, Ui kutsuu [RunCalendarService](https://github.com/ah-pasila/ot-running-calendar/blob/master/src/services/run_calendar_service.py)-luokkaa. 

Miinuksena rakenteen osalta se, että paljon syötteisiin liittyvää virhekäsittelyä jäi vain käyttöliittymän puolelle. Toisena isompana miinuksena vaatimusmäärittelyssä tavoitteena oli toteuttaa graafinen käyttöliittymä, mikä on harmillinen puute. 

## Luokat User ja Plan sekä sovelluslogiikka RunCalendarService

Sovelluksessa on luokat [User](https://github.com/ah-pasila/ot-running-calendar/blob/master/src/entities/user.py) eli käyttäjä ja [Plan](https://github.com/ah-pasila/ot-running-calendar/blob/master/src/entities/run.py) eli suunniteltu juoksu.

```mermaid
 classDiagram
    User "1" -- "*" Run

    class User{
        String username
        String password
        String gender
        Int age
    }

    class Run{
        String day
        String run_type
        Int duration
        Int length
        String description
        String username
    }
```

Sovellustoiminnot ovat luokassa [RunCalendarService](https://github.com/ah-pasila/ot-running-calendar/blob/master/src/services/run_calendar_service.py), joka viittaa niin User-, Plan- kuin repositorioluokkiinkin. 

## Tietojen tallennus - repositoriot

Tietojen tallentamisesta tietokantaan vastaavat käyttäjätietojen osalta [User_repository](https://github.com/ah-pasila/ot-running-calendar/blob/master/src/repositories/user_repository.py) ja juoksujen osalta [Run_Repository](https://github.com/ah-pasila/ot-running-calendar/blob/master/src/repositories/run_repository.py). 

Tiedot tallennetaan paikalliseen SQLite-tietokantaan. Tietokanta täytyy käyttöönoton yhteydessä alustaa [initialize_database.py](https://github.com/ah-pasila/ot-running-calendar/blob/master/src/initialize_database.py) ja myös, jos se jostain syystä halutaan resetoida myöhemmin. Tietokanta muodostuu sovelluskansion juureen data-kansioon. 

Tietokannan taulujen määrittelyt (id:t generoituvat automaattisesti):
```
id INTEGER PRIMARY KEY AUTOINCREMENT,
username TEXT UNIQUE NOT NULL,
password TEXT NOT NULL,
gender TEXT,
age INTEGER
```

```
id INTEGER PRIMARY KEY AUTOINCREMENT,
day TEXT NOT NULL,
type TEXT NOT NULL,
duration INTEGER,
length INTEGER,
description TEXT,
username TEXT
```

## Toimintalogiikka

Sovelluksen perustoimintalogiikka on, että käyttöliittymä pyytää käyttäjältä syötteitä ja validoi ne. Syötteet viedään eteenpäin juoksukalenterisovellusluokalle, joka edelleen kutsuu repositorioluokkia joko tietojen tallentamista ja palauttamista eli tarkistamista tai tulostamista varten. Esimerkkinä kuvattu alla sekvenssikaaviona uuden käyttäjän luominen, johon liittyy sekä tiedon tarkistamista että tallentamista. 

### Uuden käyttäjän luominen

```mermaid
sequenceDiagram
    actor AppUser
    participant UI
    participant RunCalendarService
    participant User_repository
    participant User
    AppUser->>UI: "Testinimi"
    UI->>RunCalendarService: check_username("Testinimi")
    RunCalendarService->>User_repository: check_username_exists("Testinimi")
    User_repository-->>RunCalendarService:False
    RunCalendarService-->>UI: False
    AppUser->>UI: "Testinimi", "Testisala", "f", "40"
    UI->>RunCalendarService: add_user("Testinimi","Testisala","f","40")
    RunCalendarService->>User: User("Testi","Testisala","f","40") 
    RunCalendarService->>User_repository: add_user(User)
    User_repository-->>RunCalendarService: user
```

## Puutteita 

Luokkien välisissä suhteissa riippuvuuksien injektointi jäi hieman hieman keskeneräiseksi ja epäselväksi, mutta käsittääkseni riippuvuudet repositorioista on injektoitu RunCalendarService-luokkaan, muita riippuvuuksia ei. 

.env-konfiguraatiotiedosto, jonka avulla olisi vointu muuttaa sovelluksen konfiguraatioita, esim. tietokannan tallennuspaikka, jäi toteuttamatta. 

Kirjautuneena olevan käyttäjän toteutusmalli on hieman kömpelö; se perustuu uuteen User-olioon, johon kirjataan viimeksi kirjautuneen käyttäjän salasana (pois kirjautumisen yhteydessä ) Tietoa hyödynnetään mm. tallenuksissa. Käsittääkseni tämä aiheuttaa tilanteen, jossa sovelluksen käyttäjien tulee olla peräkkäisiä eli edellisen käyttäjän on kirjauduttava ulos ennen seuraavan aloittamista, jotta oikean käyttäjän tiedot tallentuvat esimerkiksi juoksujen yhteyteen.

Alun perin tarkoitus oli luoda laajempi luokkarakenne niin, että olisi ollut olemassa vielä RunPlan-luokka, johon olisi voinut liittää harjoitusohjelmakokonaisuuksia. Tämän vuoksi nimeämisiin jäi epäyhtenäisyyttä Run ja Plan-termien välillä.