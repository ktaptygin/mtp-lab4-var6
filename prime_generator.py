# задание 6 (среднее): генератор простых чисел

def is_prime(n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


def prime_gen():
    n = 2
    while True:
        if is_prime(n):
            yield n
        n += 1


gen = prime_gen()
print("первые 10 простых:", [next(gen) for _ in range(10)])

# ну и до 50 заодно
primes50 = []
for p in prime_gen():
    if p >= 50:
        break
    primes50.append(p)
print("простые до 50:", primes50)
