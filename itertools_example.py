import itertools
import time
from typing import Callable

max_value = int(1e+7)


def main() -> None:

    # exec(itertools_count, 'itertools count')
    # exec(range_count, 'range count')
    #
    # exec(itertools_map, 'itertools map')
    # exec(plain_map, 'range map')
    #
    # exec(itertools_repeat, 'itertools repeat')
    # exec(plain_repeat, 'range repeat')

    # exec(itertools_chain, 'itertools chain')
    # exec(plain_chain, 'itertools chain')

    exec(itertools_takewhile, 'itertools takewhile')
    exec(plain_takewhile, 'plain takewhile')

    exec(itertools_starmap, 'itertools starmap')
    exec(plain_starmap, 'plain starmap')

# region count
def itertools_count():
    global max_value
    numbers = itertools.count(0, 1)
    res = 0
    for i in numbers:
        if i == max_value:
            break
        res += i


def range_count():
    global max_value
    res = 0
    for i in range(max_value):
        res += i
# endregion

# region repeat

def itertools_repeat():
    global max_value
    val = 10
    l1 = itertools.repeat(val, times=max_value)
    res = 0
    for i in l1:
        res += i
    print(res)

def plain_repeat():
    global max_value
    val = 10
    res = 0
    for i in range(max_value):
        res += val
    print(res)
# endregion

# region map
def itertools_map() -> None:
    l1 = map(lambda x: x ** 2, itertools.count())
    res = 0
    for index, i in enumerate(l1):
        if index == max_value:
            return
        res += i


def plain_map() -> None:
    l1 = [i for i in range(max_value)]
    map(lambda x: x ** 2, l1)
    res = 0
    for index, i in enumerate(l1):
        if index == max_value:
            return
        res += i
# endregion

# region execute computing execution time
def exec(f: Callable[[], None], label: str) -> None:
    start = time.time()
    f()
    print(f'{label} time: {time.time() - start}')
# endregion

# region chain
def itertools_chain():
    multiplier = int(1e+6)
    l = itertools.chain([1, 2, 3] * multiplier,
                        [4, 5, 6] * multiplier,
                        [7, 8, 9] * multiplier)
    res = 0
    for val in l:
        res += val


def plain_chain():
    multiplier = int(1e+6)
    l1 = [1, 2, 3] * multiplier
    l2 = [4, 5, 6] * multiplier
    l3 = [7, 8, 9] * multiplier
    l = l1 + l2 + l3
    res = 0
    for val in l:
        res += val

# endregion


# region take while
def itertools_takewhile():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] * int(1e+6)
    odd = itertools.takewhile(lambda x: x % 2 != 0, numbers)
    for i in odd:
        pass

def plain_takewhile():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9] * int(1e+6)
    odd = []
    for number in numbers:
        if number % 2 != 0:
            odd.append(number)
    for i in odd:
        pass
# endregion

# region star map
def itertools_starmap():
    args = [(1, 2), (3, 4), (5, 6)] * int(1e+6)
    l1 = itertools.starmap(pow, args)
    for i in l1:
        pass


def plain_starmap():
    args1 = [1, 3, 5] * int(1e+6)
    args2 = [2, 4, 6] * int(1e+6)
    l1 = map(pow, args1, args2)
    for i in l1:
        pass

# endregion

if __name__ == '__main__':
    main()
