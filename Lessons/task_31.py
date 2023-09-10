# Последовательностью Фибоначчи называется
# последовательность чисел a0, a1, ..., an, ..., где a0 = 0, a1 = 1, ak = ak-1 + ak-2 (k > 1).
# Требуется найти N-е число Фибоначчи
# Input: 7
# Output: 21
# Задание необходимо решать через рекурсию


def fib(n):
    return fib(n - 2) + fib(n - 1) if n > 2 else 1


print(fib(7))


def fibo(n):
    return n if n < 3 else fibo(n - 1) + fibo(n - 2)


print(fibo(7))

f1 = 1
f2 = 2

n = 7
n = n - 2
while n > 0:
    f1, f2 = f2, f1 + f2
    n -= 1

print(f2)

# 0 1 1 2 3 5 7 13 21 34
