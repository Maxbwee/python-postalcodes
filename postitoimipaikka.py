# Esimerkkisuoritus:
#
# Kirjoita postinumero: 00100
# HELSINKI
import urllib.request
import json


def hae_postinumerot():
    with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        data = response.read()

    postinumerot = json.loads(data)
    return postinumerot


kysely = input("Syötä postinumero:")

data = hae_postinumerot()

if kysely in data:
    print(data[kysely])

else:
    print("Tuntematon postinumero")
