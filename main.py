import time
from threading import Thread
from typing import Tuple

delay = 0.2

numbers = [10, 4, 5, 6, 3, 12, 1]
res = [0] * len(numbers)


def factorial(index: int):
    # global res, numbers
    res[index] = 1
    for i in range(1, numbers[index] + 1):
        time.sleep(delay)
        res[index] *= i


def main():
    calc_parallel()
    calc_plain()


def calc_parallel():
    print(f'Start of {calc_parallel.__name__}')
    start = time.time()

    threads = []
    for i in range(len(numbers)):
        # create thread
        thread = Thread(target=factorial, args=(i,))
        # start thread
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    for i, number in enumerate(numbers):
        print(f'factor of {number} is {res[i]}')

    print(f'End of {calc_parallel.__name__}, Time: {time.time() - start}')


def calc_plain():
    print(f'Start of {calc_plain.__name__}')
    start = time.time()
    for i in range(len(numbers)):
        factorial(i)

    print(f'End of {calc_plain.__name__}, Time: {time.time() - start}')


if __name__ == '__main__':
    main()
