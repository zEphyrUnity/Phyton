# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2 в степени), не превосходящие числа N.
# 10 -> 1 2 4 8

N = 10


def powers_of_two(n):
    i = 0
    powers_list = []

    while pow(2, i) < n:
        powers_list.append(pow(2, i))
        i += 1

    return powers_list


print(N, "->", *powers_of_two(N))