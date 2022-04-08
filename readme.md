# Python-postinumerot

Tämän koodaustehtävän tavoitteena on luoda pohja seuraavien viikkojen tehtäville, joissa käsittelemme dataa ja testaamme ohjelmistoja Python-kielellä. Kaikkien mahdollisten Pythonin rakenteiden opetteleminen etukäteen ei ole kurssin kannalta tarkoituksenmukaista, joten tässä tehtäväksi on valittu sellainen, jonka kautta opimme soveltamaan Pythonin perusrakenteita.

Tehtävät arvostellaan käyttäen [GitHub classroom](https://classroom.github.com/) -palvelua, joka suorittaa komentosi, ja tarkastaa ja pisteyttää niiden tulokset automaattisesti. Taustalla GitHub classroom hyödyntää [GitHub actions](https://github.com/features/actions) -nimistä jatkuvan integroinnin palvelua. Voit tarvittaessa yrittää tehtäviä monta kertaa. Tee tällöin uusi commit, ja vie muutokset uudelleen GitHubiin.

Tehtävien toimintalogiikan ja käyttöliittymän ei tarvitse noudattaa pilkulleen annettuja esimerkkejä, mutta toimintalogiikan tulee olla samankaltainen. Automaattisen arvioinnin vuoksi ohjelmasi tulee toimia täsmälleen samoilla syötteillä kuin esimerkit.


## Harjoitusten kloonaaminen

Kun olet hyväksynyt tehtävän GitHub classroomissa ja saanut repositoriosta henkilökohtaisen kopion, kloonaa se itsellesi `git clone` -komennolla. Siirry sen jälkeen VS Codeen editoimaan tiedostoja.

Kloonatessasi repositoriota varmista, että Git-osoitteen lopussa on oma GitHub-käyttäjänimesi. Jos käyttäjänimesi puuttuu osoitteesta, kyseessä ei ole henkilökohtainen kopiosi tehtävästä. Luo tässä tapauksessa oma repositorio tämän linkin kautta: https://classroom.github.com/a/sk7RyyX1.


## Vastausten lähettäminen

Kun olet saanut toisen tai molemmat tehtävät ratkaistua, lisää tiedostoihin tekemäsi muutokset versionhallintaan `git add` ja `git commit` -komennoilla. Lähetä ratkaisut arvioitavaksi `git push`-komennolla. Git push käynnistää automaattisesti workflow:n, joka testaa kaikki komentosi ja antaa niistä joko hyväksytyn tai hylätyn tuloksen.

Kun GitHub Actions on saanut koodisi suoritettua, näet tuloksen GitHub-repositoriosi [Actions-välilehdellä](../../actions/workflows/classroom.yml). Arvioinnin valmistumiseen menee tyypillisesti noin pari minuuttia.

Klikkaamalla yllä olevan linkin takaa viimeisintä "GitHub Classroom Workflow" -suoritusta, saat tarkemmat tiedot tehtävän arvioinnista. Sivun alaosassa näkyy saamasi pisteet. Klikkaamalla "Autograding"-otsikkoa pääset katsomaan tarkemmin arvioinnissa suoritetut vaiheet ja niiden tulokset.


# Postinumeroaineisto

GitHubista löytyy valmis projekti https://github.com/theikkila/postinumerot, jonka avulla voidaan hakea Postin tietokannasta kaikki postinumerotiedot. Projektissa on myös mukana valmiiksi koostettuja JSON-tiedostoja postinumeroista. 

> *"Data on postin ja sitä koskee kaikki http://www.posti.fi/liitteet-yrityksille/ehdot/postinumeropalvelut-palvelukuvaus-ja-kayttoehdot.pdf dokumentin käyttöehdot."*
>
> *"JSON-muunnokset ovat vapaasti käytettävissä ja muunneltavissa."*
>
> Lähde: https://github.com/theikkila/postinumerot


Tässä tehtävässä sinun tulee käyttää postinumerotiedostoa [postcode_map_light.json](https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json), joka sisältää JSON-olion, jossa postinumerot ovat avaimia ja postitoimipaikat arvoja, esimerkiksi:

```json
{
    "74701": "KIURUVESI",
    "35540": "JUUPAJOKI",
    "74700": "KIURUVESI",
    "73460": "MUURUVESI"
}
```

JSON-muotoisen merkkijonon parsiminen Pythonin tietorakenteiksi onnistuu standardikirjaston `json`-kirjastolla: https://docs.python.org/3/library/json.html:

```python
>>> import json
>>>
>>> json.loads("""{
...     "74701": "KIURUVESI",
...     "35540": "JUUPAJOKI",
...     "74700": "KIURUVESI",
...     "73460": "MUURUVESI"
... }""")
{'74701': 'KIURUVESI', '35540': 'JUUPAJOKI', '74700': 'KIURUVESI', '73460': 'MUURUVESI'}
>>>
```


# Osa 1: Postitoimipaikka (2 pistettä)

Kirjoita Python-kielinen ohjelma `postitoimipaikka.py`, joka kysyy  käyttäjältä postinumeron ja kertoo, mihin postitoimipaikkaan kyseinen postinumero kuuluu.

Tehtävän ratkaisemiseksi sinun tulee kysyä käyttäjältä syötettä ja etsiä postinumeroaineistosta syötettä vastaava arvo. Voit joko tallentaa postinumeroaineiston koneellesi ja [lukea sen levyltä](https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files) tai toteuttaa ohjelmasi [lukemaan tiedoston suoraan verkosta](https://docs.python.org/3/howto/urllib2.html).

Esimerkkisuoritus:

    $ python3 postitoimipaikka.py
    
    Kirjoita postinumero: 00100
    HELSINKI

Mikäli annettua postinumeroa ei löydy aineistosta, ohjelmasi tulee tulostaa teksti "Tuntematon postinumero".

Vinkit:
* Mikäli luet tiedot tallennetusta tiedostosta, muista lisätä kyseinen tiedosto myös versionhallintaan.
* Tulosteen kirjainkoolla ei ole merkitystä.


# Osa 2: Postinumerot (3 pistettä)

Kirjoita Python-kielinen ohjelma `postinumerot.py`, joka kysyy käyttäjältä postitoimipaikan nimen, ja listaa kaikki kyseisen postitoimipaikan postinumerot **kasvavassa järjestyksessä**.

Tehtävän voi ratkaista useilla tavoilla, joten käytä hetki ongelman pohtimiseen ennen kuin ryhdyt koodaamaan. Olisiko esimerkiksi helpompaa jäsentää postinumeroaineisto etukäteen uudenlaiseksi tietorakenteeksi, vai käydä avain-arvo-pareja läpi yksi kerrallaan postinumeroiden löytämiseksi. Seuraavalla viikolla käsittelemme hieman lähemmin tietorakenteiden ja algoritmien suunnittelua ja tehokkuutta.

Esimerkkisuoritus:

    $ python3 postinumerot.py

    Kirjoita postitoimipaikka: Porvoo
    Postinumerot: 06100, 06101, 06150, 06151, 06200, 06400, 06401, 06450, 06500

Toteuta ohjelma siten, että syötetyn postitoimipaikan kirjainkoolla ei ole merkitystä. Huolehdi myös siitä, että tuntemattoman nimen syöttäminen ei kaada ohjelmaa, vaan tulostaa tekstin 'Tuntematon postitoimipaikka'.


# Lähteitä

Pythonin dict-tietorakenne, eli sanakirja, muistuttaa Javan map-tietorakennetta. Tulet tarvitsemaan sanakirjaa tausta-aineiston käsittelemisessä: https://docs.python.org/3/tutorial/datastructures.html#dictionaries

Tiedoston lataaminen verkosta onnistuu esim Python 3: standardikirjastoon kuuluvalla `urllib`-kirjastolla: https://docs.python.org/3/howto/urllib2.html.

JSON-muotoisen merkkijonon parsiminen Pythonin listoiksi, sanakirjoiksi ja muiksi tietorakenteiksi onnistuu standardikirjaston `json`-kirjastolla: https://docs.python.org/3/library/json.html
