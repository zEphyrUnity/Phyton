# Напишите функцию f, которая на вход принимает два числа a и b,
# и возводит число a в целую степень b с помощью рекурсии.
#
# Функция не должна ничего выводить, только возвращать значение.
#
# Пример:
#
# a = 3; b = 5 -> 243 (3⁵)
# a = 2; b = 3 -> 8


import timeit

my_func = '''def f(a, b):
    if b <= 1:
        return a
    return a * f(a, b - 1)'''

my_super_func = '''def f(a, b):
    if b == 1:
        return a
    if b % 2 == 0:
        print("чет")
        result = f(a, b // 2)
        return result * result

    if b % 2 == 1:
        print("нечет")
        result = f(a, b // 2)
        return result * result * a'''


# print(f(3, 996))
print(timeit.timeit(stmt=my_func, setup="", number=10000))
print(timeit.timeit(stmt=my_super_func, setup="", number=10000))
