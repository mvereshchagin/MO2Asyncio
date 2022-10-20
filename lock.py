from multiprocessing import Process
import time
from threading import Thread, Lock
from typing import List, Callable

counter = 0
max_value = 15
process_count = 4
iter_sleep = 0.2

lock = None


def change_counter(pid: int) -> None:
    global counter

    sleep = 2

    # print(f'{pid} starts')
    time.sleep(sleep)
    # print(f'{pid} resumes')
    if lock is not None:
        with lock:
            do_counter()
    else:
        do_counter()


def do_counter() -> None:
    global counter
    for i in range(max_value):
        time.sleep(iter_sleep)
        counter += 1


def main() -> None:

    numbers = [i for i in range(process_count)]

    processes = [Process(target=run, args=(plain, numbers, 'plain')),
                 Process(target=run, args=(threads_no_lock, numbers, 'no lock')),
                 Process(target=run, args=(threads_with_lock, numbers, 'with lock'))]

    for p in processes:
        p.start()


def plain(numbers: List[int]) -> None:
    for number in numbers:
        change_counter(number)


def threads_no_lock(numbers: List[int]) -> None:
    global lock
    lock = None

    threads = [Thread(target=change_counter, args=(number,)) for number in numbers]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def threads_with_lock(numbers: List[int]) -> None:
    global lock
    lock = Lock()

    threads = [Thread(target=change_counter, args=(number,)) for number in numbers]
    for thread in threads:
        thread.start()

    for thread in threads:
        thread.join()


def run(func: Callable[[List[int]], None], numbers: List[int], label: str) -> None:
    start = time.time()
    func(numbers)
    print(f'{label}: executing time = {time.time() - start}')


if __name__ == '__main__':
    main()
