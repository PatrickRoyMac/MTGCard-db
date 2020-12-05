##Get data from Scryfall api

##TO-DO LIST
#Backend - 
#Save Data output to a database
#Image recognition of the card
#Use Image to search for the card
#Card validation by the User
#Frontend - 
#Make a front end that shows what cards the user has
#Front end can search for cards in MTG library
#Front end simple login 


import requests
from requests.exceptions import HTTPError

card_name="anjie Falkenrath"
card_name_format=card_name.replace(" ","%2b")

url = "https://api.scryfall.com/cards/named?fuzzy={}".format(card_name_format)
def scry_resp():

    try:
        reponse = requests.request("GET", url)
        reponse.raise_for_status()
        #access Json Content
        jsonResponse = reponse.json()
        for key, value in jsonResponse.items():
            print(key, ":", value)

    except HTTPError as http_err:
        print(f'HTTP error Occured: {http_err}')
    except Exception as err:
        print(f'HTTP error Occured: {err}')

