# Vaatimusmäärittely

## Sovelluksen käyttötarkoitus

Sovellluksen ominaisuuksien toteutumista palautusversiossa on tarkasteltu seuraavien otsikoiden alla ja toteutetut ominaisuudet on merkitty (x).

Sovellusta käytetään henkilökohtaisen juoksukalenterin suunnitteluun. Päästäkseen suunnittelemaan juoksukalenteria, käyttäjän on kirjauduttava sovellukseen (x). Tämän jälkeen käyttäjä merkitsee omaan viikkokalenteriinsa tulevan viikon harjoituksensa eri vaihtoehdoista (juoksu/pyöräily/kävely/uinti/lihaskunto/lihashuolto/muu) (x osin; vain juoksu). Käyttäjä koostaa harjoitusviikon lisäämällä halutut harjoitukset ja niiden pituuden/keston (x). Sovellus laskee arvion kertyvistä viikkokilometreistä/harjoitustunneista sekä erikseen nimenomaan juoksusta kertyvän harjoitteluajan ja matkan (x; osin, laskenta halutulta ajanjaksolta, käytössä vain juoksu). 

## Käyttäjät

Alussa sovelluksella on vain peruskäyttäjiä (x). Erillinen admin-rooli lisätään tarvittaessa myöhemmin.

## Käyttöliittymä

Sovelluksessa tulee olemaan kirjautumisikkuna, käyttäjätunnuksen luonti-ikkuna ja omassa ikkunassaan viikkonäkymä (ei toteutunut, tekstipohjainen ui).

## Perustoiminnot

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen ja salasanan (x)
  - Molempien oltava vähintään 8-merkkisiä (x osin; vaatimus vain salasanalla), lisäksi käyttäjätunnuksen oltava ainutkertainen (x).
- Käyttäjä voi kirjautua järjestelmään määrittelemällään käyttäjätunnuksella ja salasanalla (x).
- Kirjautumisen jälkeen käyttäjä näkee tyhjän viikkonäkymän (ei toteutunut ajatellusti).
  - Oletuksena näkyy kuluva viikko
  - Käyttäjä voi vaihtaa toiseen viikkoon
- Käyttäjä voi valita viikonpäiville sopivat harjoitukset valmiista vaihtoehdoista sekä halutessaan lisätä niille keston ja matkan (x osin; vain omien juoksuharjoitusten lisäys mahdollista). 
- Käyttäjä voi tallentaa viikkosuunnitelmansa, jolloin siihen on seuraavalla kerralla mahdollista palata (x).
- Käyttäjä voi kirjautua ulos jäjestelmästä ohjelman sulkemisen yhteydessä (x; käyttäjä kirjataan ulos).


## Jatkokehitysideat

Mahdollisia täydennyksiä:

- Käyttäjä voi itse lisätä uusia lajeja.
- Käyttäjä voi vaihtaa viikkotason näkymästä kuukausi-/vuosinäkymään (x; toteutunut osin, käyttäjä voi tutkia haluamansa ajanjaksoa).
- Sovelluksessa on tarjolla valmiita harjoitusohjelmaehdotuksia perustuen käyttäjän valintaan eli onko käynnissä peruskunto-, kilpailuun valmistava, kilpailu- tai ylimenokausi.
- Käyttäjä voi merkita toteutuneen liikunnan ja seurata toteumia (esim. juoksukilometrit suhteessa suunniteltuihin ja toteuma-%:n laskenta).
- Käyttäjä voi vaihtaa salanansa.
- Erillisen admin-roolin toteutus peruskäyttäjien tilien hallintaan ja suunnitelmien seurantaan.
