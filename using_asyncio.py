import asyncio
import time
from typing import List


def fibonacci(i: int) -> int:

    if i == 0:
        return 0
    if i == 1:
        return 1

    return fibonacci(i - 1) + fibonacci(i - 2)


async def fibonacci_async(number: int):
    ioloop = asyncio.get_event_loop()
    res = await ioloop.run_in_executor(None, fibonacci, number)
    return res


async def long_operation() -> None:
    print('Start long operation')
    await asyncio.sleep(1)
    print('End long operation')


async def start_without_waiting() -> None:
    print('Start main')
    ioloop = asyncio.get_event_loop()
    task = ioloop.create_task(long_operation())
    # asyncio.sleep(1)
    # asyncio.run(long_operation())
    # ioloop.close()
    print('End main')


async def main():
    # asyncio.run(start_without_waiting())
    start = time.time()
    res = await calc_list_of_fibonacci([37, 34, 35])

    # asyncio.run(calc_list_of_fibonacci([37, 34, 35]))

    # res = [fibonacci(number) for number in [37, 34, 35]]
    print(res)

    print(f'time = {time.time() - start}')


async def calc_list_of_fibonacci(numbers: List[int]):
    ioloop = asyncio.get_event_loop()
    tasks = [fibonacci_async(i) for i in numbers]
    res = await asyncio.gather(*tasks)
    print(res)


if __name__ == '__main__':
    asyncio.run(main())