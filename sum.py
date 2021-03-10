def first(n):
    num = 1
    total = 0
    while num < n + 1:
        total = total + num
        num = num + 1
    return total


print(first(5))


def better(n):
    total = 0
    for num in range(n + 1):
        total += num
    return total


print(better(10))


def even_better(n):
    return sum(range(n + 1))


print(even_better(10))


def add_it_up(n):
    try:
        result = sum(range(n + 1))
    except TypeError:
        result = 0
    return result


print(add_it_up(5))
