# api asynchrocznicznie z kluczem

import prywatne as p
import asyncio
import aiohttp

async def get_data_async(base_url, params, headers):
    async with aiohttp.ClientSession() as session:
        async with session.get(base_url, headers=headers, params=params) as response:
            data = await response.json()

            if response.status == 200:
                print("DLA: ", base_url, ": ")
                for key, value in data.items():
                    print(key, ":", value)
                    print()

            else:
                print(f"Error: {data.get('message', 'Unknown error')}")


async def main():
    base_url_weather = "http://api.weatherapi.com/v1/current.json"
    api_key_weather = p.api_weather()
    params_weather = {
        'key' : api_key_weather,
        'q': 'Warsaw',
        'aqi': 'no'
    }

    base_url_finance = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/auto-complete"
    api_key_finance = p.api_finance()
    params_finance = {
        'q' : 'tesla',
        'region' : 'US'
    }
    headers_finance = {
        'X-RapidAPI-Key': api_key_finance,
        'X-RapidAPI-Host': 'apidojo-yahoo-finance-v1.p.rapidapi.com'
    }

    tasks = [
        get_data_async(base_url_weather, params_weather, None),
        get_data_async(base_url_finance, params_finance, headers_finance)
    ]

    await asyncio.gather(*tasks)

asyncio.run(main())