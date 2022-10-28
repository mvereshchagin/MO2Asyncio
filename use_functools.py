from functools import wraps, reduce
from operator import mul, add
import time
import random


def main():
    calc_sum_reduce()
    calc_sum_plain()

    calc_max_reduce()
    calc_max_reduce_def()
    calc_max_max()
    calc_max_plain()


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds')
        return result
    return timeit_wrapper


@timeit
def calc_sum_reduce():
    arr = [1, 2, 3] * int(1e+6)
    # res = reduce(lambda x, y: x + y, arr)
    res = reduce(add, arr)
    print(res)


@timeit
def calc_sum_plain():
    arr = [1, 2, 3] * int(1e+6)
    res = 0
    for i in arr:
        res += i
    print(res)


@timeit
def calc_max_reduce():
    size = int(1e+6)
    arr = [random.randint(1, 1000) for i in range(size)]
    max_value = reduce(lambda a, b: a if a > b else b, arr)
    print(max_value)

@timeit
def calc_max_reduce_def():
    size = int(1e+6)
    arr = [random.randint(1, 1000) for i in range(size)]
    max_value = reduce(compare, arr)
    print(max_value)

def compare(a, b):
    return a if a > b else b

@timeit
def calc_max_max():
    size = int(1e+6)
    arr = [random.randint(1, 1000) for i in range(size)]
    max_value = max(arr)
    print(max_value)

@timeit
def calc_max_plain():
    size = int(1e+6)
    arr = [random.randint(1, 1000) for i in range(size)]
    max_value = -1
    for val in arr:
        if val > max_value:
            max_value = val
    print(max_value)


if __name__ == '__main__':
    main()