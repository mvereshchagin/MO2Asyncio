from multiprocessing import Process, Value, Pool, Queue
import time
from typing import List


def fibonacci(i: int) -> int:
    if i == 0:
        return 0
    if i == 1:
        return 1

    return fibonacci(i - 1) + fibonacci(i - 2)


def run_fibonacci(i: int, ret_value: Value):
    ret_value.value = fibonacci(i)


def run_fibonacci_pool(i: int):
    res = fibonacci(i)
    return i, res


def main():
    number = 10
    # calc(number=number, parallel=False)
    # calc(number=number, parallel=True)

    numbers = [35, 35, 35, 35, 35, 35]
    calc_many('plain', numbers, parallel=False)
    calc_many('parallel', numbers, parallel=True)


def calc(number: int, parallel: bool):
    start = time.time()
    res = 1
    if not parallel:
        res = fibonacci(number)
    else:
        ret_value = Value('i', 1, lock=False)
        process = Process(target=run_fibonacci, args=(number, ret_value))
        process.start()
        process.join()
        res = ret_value.value
    print(f'{res} for {number}, time: {time.time() - start}')


def calc_many(name: str, numbers: List[int], parallel: bool = False):
    start = time.time()
    if not parallel:
        for number in numbers:
            res = fibonacci(number)
            print(f'f[{number}] = {res}')
    else:
        pool = Pool()
        for number, res in pool.map(run_fibonacci_pool, numbers):
            print(f'f[{number}] = {res}')

    print(f'{name} exec time: {time.time() - start}')


if __name__ == '__main__':
    main()
