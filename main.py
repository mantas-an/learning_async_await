#Pagrindiniai terminai:

# async - funkcija, kuri gali buti sustabdyta ir vel paleista
# await - laukia, kol async funkcija baigs darba

# asyncio - python biblioteka asinchroniniam (leidzia nelaukiant kol viena uzduotis baigsis
# pries pradedant kita) programavimui.

#Papildoma terminologija

# aiohttp - Leidzia GET request is HTTP




#                     ASINCHRONINIS


import asyncio

async def pasisveikinti(vardas, laukimo_laikas):
    print(f'Pradedu {vardas}...')
    await asyncio.sleep(laukimo_laikas) # simuliuojam uzduoti
    print(f'{vardas} baige darbus!')


async def main():
    # 3 funkciju paleidimas
    task1 = asyncio.create_task(pasisveikinti('Funkcija a', 3))
    task2 = asyncio.create_task(pasisveikinti('Funkcija b', 2))
    task3 = asyncio.create_task(pasisveikinti('Funkcija c', 1))

    await task1
    await task2
    await task3

#programos paleidimas
asyncio.run(main())




#            COROUTINE

# async def main():
#     #async itraukia funkcija i deze, kuria pakvietus grazins COROUTINE objekta. kad execute Coroutine mum reikes await.
#     #await turi buti viduje Asinchronineje funkcijoje
#     print('Mantas')
#     await dede("tekstas") #await sioje vietoje neleidzia pereiti prie kito print.
#     print("Pabaigta") #nustacius aysncio.sleep gauname sia zinute.
#
# async def dede(text):
#     print(text)
#     await asyncio.sleep(5)
#
# #main() # jeigu be await gausime warning coroutine 'main' was never awaited main()
# asyncio.run(main()) #kad paleistume asinchronine coroutine. P.S Tai sukuria event loop.
