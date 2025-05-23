# api synchronicznie bez klucza

import requests
import asyncio 
import json

async def import_data(url):

    response = requests.get(url)

    if response.status_code != 200:
        raise print("Request failed")
    
    else:
        data = response.json()
        for row in data['entries']:
            print(row['Link'])

        with open("api.json", "w") as outfile: 
            json.dump(data, outfile)


asyncio.run(import_data("https://api.publicapis.org/entries"))

