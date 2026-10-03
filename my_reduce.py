# задание 10 (повышенное): написать собственный reduce

def my_reduce(func, seq, init=None):
    it = iter(seq)
    if init is None:
        acc = next(it)  # берём первый элемент
    else:
        acc = init
    for x in it:
        acc = func(acc, x)
    return acc


nums = [1, 2, 3, 4, 5, 6]

print("сумма:", my_reduce(lambda a, b: a + b, nums))
print("произведение:", my_reduce(lambda a, b: a * b, nums))
print("максимум:", my_reduce(lambda a, b: a if a > b else b, nums))
