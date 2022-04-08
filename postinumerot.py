# Esimerkkisuoritus:
#
# Kirjoita postitoimipaikka: Porvoo
# Postinumerot: 06100, 06101, 06150, 06151, 06200, 06400, 06401, 06450, 06500
import urllib.request
import json


def hae_postinumerot():
    with urllib.request.urlopen('https://raw.githubusercontent.com/theikkila/postinumerot/master/postcode_map_light.json') as response:
        data = response.read()

    postinumerot = json.loads(data)
    return postinumerot


def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = []
    listOfItems = dictOfElements.items()
    for item in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return listOfKeys


def listToString(listOfKeys):
    str = ''
    for alkio in listOfKeys:
        str += alkio
        str += ', '
    mod_string = str[:len(str) - 2]
    return mod_string


kysely = input("Kirjoita postitoimipaikka: ")
data = hae_postinumerot()
kysely = kysely.upper()
listOfKeys = getKeysByValue(data, kysely)
listOfKeys.sort()
if len(listOfKeys) == 0:
    print("Tuntematon postitoimipaikka")
else:
    print("Postinumerot: " + listToString(listOfKeys))


#arr = [num for num in data if data[num] == kysely]

# print(int(arr[data]))

#kysely = kysely.upper()

# if kysely in arr:
#    print(arr[data])
