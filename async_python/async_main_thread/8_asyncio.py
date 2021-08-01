

# рассматриваем событийные циклы
# 1. asyncio - фреймворк для создания событийных циклов
# 2. Пример простой асинхронной программы для python 3.4.
# 3. Синтаксис async/await на замену @asyncio.coroutine и yield from
# 4 пример асинхронной загрузки файлов


# пишем две функции 1-ая should print numbers by 1 to infinity
# just print curent time every time after 3 seconds

import asyncio
from time import time


# @asyncio.co routine
# в python 3.5. ввели синтаксис взамен атавизма декоратора
# yield from заменили на awaiy
async def print_nums():
    num = 1
    while True:
        print(num)
        # функция ассинхронная (не блокирует выполнение программы), имеем генератор
        # python 3.4. old
        # yield from asyncio.sleep(1)
        # python 3.5. +
        await asyncio.sleep(1)
        num += 1


# @asyncio.coroutine
async def print_time():
    count = 0
    while True:
        if count % 3 == 0:
            print("{} seconds have passed".format(count))
        count += 1
        # yield from asyncio.sleep(1)
        await asyncio.sleep(1)

# @asyncio.coroutine
async def main():
    # до 3.6.
    # task1 = asyncio.ensure_future(print_nums())
    # после 3.6.
    task1 = asyncio.create_task(print_nums())
    # task2 = asyncio.ensure_future(print_time())
    task2 = asyncio.create_task(print_time())
    # yield from asyncio.gather(task1, task2)
    await asyncio.gather(task1, task2)


if __name__ == "__main__":
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())
    # loop.close()

    asyncio.run(main())
