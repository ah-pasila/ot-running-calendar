# Arkkitehtuuri

## Rakenne

Koodi on toistaiseksi jaettu pakkauksiin ui (käyttöliittymä), services (sovellus) ja entities (luokat). 
Käyttöliittymä kutsuu sovellusta, joka puolestaan kutsuu luokkia. Tietojen pysyväistallennusratkaisua ei ole vielä toteutetut.

## Luokkakaavio

```mermaid
 classDiagram
    User "1" -- "*" Plan
    User "1" -- "1" Run_calendar
    Plan "*" -- "1" Run_calendar

    class User{
        String username
        String password
        String gender
        int age
        +add_gender()
        +add_age()
    }

    class Plan{
        String day
        String description
        int length
        +add_run()
    }

    class Run_calendar{
       int year
    }
   
```
