# Напишите функцию, которая принимает одно число и
# проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое
# имеет 2 делителя: 1 и n(само число)
# Input: 5
# Output: yes


def is_prime(some_num):
    checker = True

    for i in range(2, some_num // 2 + 1):
        if some_num % i == 0:
            checker = False

    return checker


user_num = int(input("Введите число: "))
print("yes" if is_prime(user_num) else "no")

