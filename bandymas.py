import asyncio
import  aiohttp
from aiohttp import ClientSession


#uzduotis

# Write a script that runs two async functions concurrently:
#
# task1() prints "Task 1 started", waits 2 seconds, then prints "Task 1 finished".
#
# task2() does the same but waits 1 second.
# Use asyncio.sleep() for delays.

#Kurta ziurint i uzrasus is main.py vietos kurios reikejo paziureti,pradedant - >DEF MAIN .
# -------------------------------- 2025-07-18------------------------------
# async def uzduotis1():
#     print('Task 1 started')
#     await asyncio.sleep(2)
#     print('Task 1 finished')
#
# async def uzduotis2():
#     print('Task 2 started')
#     await asyncio.sleep(1)
#     print('Task 2 finished')
#
# async def main():
#     task1 = asyncio.create_task(uzduotis1())
#     task2 = asyncio.create_task(uzduotis2())
#
#     await task1
#     await task2
#
#
# asyncio.run(main())

# -------------------------------- 2025-07-19------------------------------


# 1. Create an async function that prints "Tick" every second for 5 seconds
#
# async def spausdinti():
#     for i in range(5):
#         print("Tick")
#         await asyncio.sleep(1)
#
# async def main():
#     task1 = asyncio.create_task(spausdinti())
#     await task1
#
# asyncio.run(main())

#Nezinojau tiksliai kur for ideti, pasinaudojau Ai.
#uZSTRIGAU TIES async def, await buvo iskart po for, todel mete 5 iskart.


# 2. Modify your existing code to run 3 tasks simultaneously with different sleep durations
#Make the main function gather all results.

# async def spausdinti1(pavadinimas, laukimas):
#
#         print(pavadinimas)
#         await asyncio.sleep(laukimas)
#         print(f"{pavadinimas} baige")
#
#
#
# async def main():
#     task1 = asyncio.create_task(spausdinti1("tick1", 1))
#     task2 = asyncio.create_task(spausdinti1("tick2", 3))
#     task3 = asyncio.create_task(spausdinti1("tick3", 2))
#
#     # await task1
#     # await task2
#     # await task3
#     await asyncio.gather(task1, task2, task3) #gather naudojam norint surinkti visus await ir maziau rasyti reikes :)
#
# asyncio.run(main())






# Simple HTTP Request:
#
# Fetch data from https://httpbin.org/get and print the response

async def fetch_url(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.json()

async def main():
    urls =  "https://httpbin.org/get"


    result = await fetch_url(urls)
    print (result)

asyncio.run(main())