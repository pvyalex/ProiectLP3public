import requests
import json
import time
lista_universitatii = ["upb.ro", "utcb.ro", "uauim.ro", "usamv.ro"]
new_data = {}

# Obținerea datelor de la API
for universitate in lista_universitatii:
    url = "https://api.builtwith.com/kw2/api.json"
    params = {
        'KEY': 'cee7f3bb-87a7-4add-acac-0ab4733e3172',
        'LOOKUP': universitate
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        domain = data['Keywords'][0]['Domain']
        keywords = data['Keywords'][0]['Keywords']
        new_data[domain] = keywords

        with open("../rezultate.txt", "a") as fisier_in:
            for i in keywords:
                fisier_in.write(i + " ")
    except requests.exceptions.HTTPError as err:
        print(f"HTTP error occurred: {err}")
    time.sleep(1)



x = open("../rezultate.txt", "w")
x.close()
