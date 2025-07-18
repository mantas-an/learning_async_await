import asyncio

#uzduotis

# Write a script that runs two async functions concurrently:
#
# task1() prints "Task 1 started", waits 2 seconds, then prints "Task 1 finished".
#
# task2() does the same but waits 1 second.
# Use asyncio.sleep() for delays.

#Kurta ziurint i uzrasus is main.py vietos kurios reikejo paziureti,pradedant - >DEF MAIN .

async def uzduotis1():
    print('Task 1 started')
    await asyncio.sleep(2)
    print('Task 1 finished')

async def uzduotis2():
    print('Task 2 started')
    await asyncio.sleep(1)
    print('Task 2 finished')

async def main():
    task1 = asyncio.create_task(uzduotis1())
    task2 = asyncio.create_task(uzduotis2())

    await task1
    await task2


asyncio.run(main())