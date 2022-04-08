
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
