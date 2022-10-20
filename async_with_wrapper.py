import asyncio
from functools import wraps, partial
import time
import concurrent.futures


def fibonacci(i: int) -> int:

    if i == 0:
        return 0
    if i == 1:
        return 1

    return fibonacci(i - 1) + fibonacci(i - 2)


def async_wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=concurrent.futures.ProcessPoolExecutor(), **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)
    return run


fibonacci_async = async_wrap(fibonacci)


async def fibonacci_counter_async(number: int):
    print(f'Start calc for {number}')
    await fibonacci_async(number)
    print(f'End calc for {number}')


async def main_async():
    numbers = [40, 40, 40]

    await asyncio.gather(*[fibonacci_counter_async(i) for i in numbers])


def main():
    numbers = [40, 40, 40]
    for i in numbers:
        res = fibonacci(i)
        print(res)


if __name__ == '__main__':
    start = time.time()
    asyncio.run(main_async())
    # main()
    end = time.time()
    print(f"Time elapse: {end - start}")