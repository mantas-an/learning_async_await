#Siek tiek pakartojimo is main.py vakarykstes temos 2025-07-18


# -----------------------------------------Tikslas:-------------------------------------

#Suprasti kaip asyncio.create_task() planuoja korutinas vienu metu
#create_task() suplanuoja korutinų vykdymą vienu metu.


import asyncio

async def pasisveikinimas(vardas, laukimas):
    await asyncio.sleep(laukimas)
    print(f'Sveiki ! {vardas}')

async def main():
     task1 = asyncio.create_task(pasisveikinimas("Mantas", 4))
     task2 = asyncio.create_task(pasisveikinimas("Sampanas", 2))
     await task1
     await task2

asyncio.run(main())







