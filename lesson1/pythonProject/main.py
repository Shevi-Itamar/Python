import functools

import time


def run_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return result

    return wrapper


def cash(func):
    cache = {}

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if (func.__name__, args[0]) in cache:
            return cache[(func.__name__, args[0])]
        res = func(*args, **kwargs)
        cache[(func.__name__, args[0])] = res
        return res

    return wrapper


@cash
@run_time
def fib(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(121))
