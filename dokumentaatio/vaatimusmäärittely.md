#Vaatimusmäärittely

##Sovelluksen käyttötarkoitus

Sovellusta käytetään henkilökohtaisen juoksukalenterin suunnitteluun. Päästäkseen suunnittelemaan juoksukalenteria, käyttäjän on kirjauduttava sovelluksen.
Tämän jälkeen käyttäjä merkitsee omaan viikkokalenteriinsa tulevan viikon harjoituksensa eri vaihtoehdoista (juoksu/pyöräily/kävely/uinti/lihaskunto/lihashuolto/muu). 
Käyttäjä koostaa harjoitusviikon lisäämällä halutut harjoitukset ja niiden pituuden/keston. Sovellus laskee arvion kertyvistä viikkokilometreistä/harjoitustunneista sekä erikseen nimenomaan juoksusta kertyvän harjoitteluajan ja matkan. 

##Käyttäjät

Alussa sovelluksella on vain peruskäyttäjiä. Erillinen admin-rooli lisätään tarvittaessa myöhemmin.

##Käyttöliittymä

Sovelluksessa tulee olemaan kirjautumisikkuna, käyttäjätunnuksen luonti-ikkuna ja omassa ikkunassaan viikkonäkymä. 

##Perustoiminnot

- Käyttäjä voi luoda järjestelmään käyttäjätunnuksen ja salasanan
 - Molempien oltava vähintään 8-merkkisiä, lisäksi käyttäjätunnuksen oltava ainutkertainen.
- Käyttäjä voi kirjautua järjestelmään määrittelemällään käyttäjätunnuksella ja salasanalla.
- Kirjautumisen jälkeen käyttäjä näkee tyhjän viikkonäkymän.
 - Oletuksena näkyy kuluva viikko
 - Käyttäjä voi vaihtaa toiseen viikkoon
- Käyttäjä voi valita viikonpäiville sopivat harjoitukset valmiista vaihtoehdoista sekä halutessaan lisätä niille keston ja matkan. 
- Käyttäjä voi tallentaa viikkosuunnitelmansa, jolloin siihen on seuraavalla kerralla mahdollista palata.
- Käyttäjä voi kirjautua ulos jäjestelmästä ohjelman sulkemisen yhteydessä.


##Jatkokehitysideat

Mahdollisia täydennyksiä:

- Käyttäjä voi itse lisätä uusia lajeja.
- Käyttäjä voi vaihtaa viikkotason näkymästä kuukausi-/vuosinäkymään.
- Sovelluksessa on tarjolla valmiita harjoitusohjelmaehdotuksia perustuen käyttäjän valintaan eli onko käynnissä peruskunto-, kilpailuun valmistava, kilpailu- tai ylimenokausi.
- Käyttäjä voi merkita toteutuneen liikunnan ja seurata toteumia (esim. juoksukilometrit suhteessa suunniteltuihin ja toteuma-%:n laskenta).
- Käyttäjä voi vaihtaa salanansa.
- Erillisen admin-roolin toteutus peruskäyttäjien tilien hallintaan ja suunnitelmien seurantaan.
