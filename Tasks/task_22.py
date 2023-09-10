# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# set_a = {2, 4, 6, 8, 10, 12, 10, 8, 6, 4, 2}
# set_b = {3, 6, 9, 12, 15, 18}

user_nums = [int(x) for x in input("Введите два числа через пробел: ").split()]
set_a = set([int(x) for x in input(f"Введите {user_nums[0]} чисел через пробел: ").split()])
set_b = set([int(x) for x in input(f"Введите {user_nums[1]} чисел через пробел: ").split()])

print(*set_a.intersection(set_b))
