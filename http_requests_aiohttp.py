

#TIKSLAS:
#Gauti kelis URL adresus vienu metu be blokavimo.

#aiohttp - leidzia asinchroniniam HTTP request

#reikalingas pip install

import asyncio
import aiohttp

async def fetch_url(url):
    async with aiohttp.ClientSession() as session: #http klientas
        async with session.get(url) as response: #be blokavimo requestas, siuncia GET request
            return await response.text() #skaito response, laukia datos

async def main():
    urls = [
        "https://jsonplaceholder.typicode.com/posts/1",
        "https://httpbin.org/get",
        "https://dog.ceo/api/breeds/image/random"
    ]
    #dabar reikia sukurti korutinas
    tasks = [fetch_url(url) for url in urls]
    #paleisti korutinas ir surinkti rezultatus
    results = await asyncio.gather(*tasks)
    print(f'Gauti {len(results)} atsakymai!')

asyncio.run(main())