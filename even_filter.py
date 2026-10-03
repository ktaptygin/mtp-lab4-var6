# задание 2 (среднее): отфильтровать чётные числа из списка

def filter_even(nums):
    return list(filter(lambda x: x % 2 == 0, nums))


numbers = list(range(1, 21))
print("исходный список:", numbers)
print("чётные:", filter_even(numbers))
