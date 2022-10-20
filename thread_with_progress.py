from tqdm import tqdm
import time
from threading import Thread
from typing import Callable

delay = 0.2
number = 10
res = 1


def factorial(number: int, f: Callable) -> None:
    global res
    res = 1
    for i in range(1, number + 1):
        time.sleep(delay)
        f()
        res *= i


def main() -> None:
    pb_range = range(1, number + 1)
    pb = tqdm(pb_range, colour='green')

    thread = Thread(target=factorial, args=(number, lambda: update_pb(pb)))
    thread.start()
    thread.join()

    print(f'Factorial of {number} is {res}')


def update_pb(pb: tqdm) -> None:
    pb.update(1)


if __name__ == '__main__':
    main()
