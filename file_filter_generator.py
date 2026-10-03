# задание 4 (повышенное): фильтрация данных из файла через генератор

def filter_file(filename, pred):
    with open(filename, encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if pred(line):
                yield line


def is_even_str(line):
    try:
        return int(line) % 2 == 0
    except ValueError:
        return False


if __name__ == "__main__":
    # чётные числа из файла
    res = list(filter_file("data/numbers.txt", is_even_str))
    print("чётные из numbers.txt:", res)

    # слова длиннее 4 букв
    res2 = list(filter_file("data/words.txt", lambda w: len(w) > 4))
    print("слова длиннее 4 букв:", res2)
