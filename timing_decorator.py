# задание 8 (среднее): декоратор замера времени работы функции

import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} выполнялась {end - start:.5f} сек")
        return result
    return wrapper


@timer
def slow_sum():
    s = 0
    for i in range(1000000):
        s += i
    return s


print("сумма 1..999999:", slow_sum())
