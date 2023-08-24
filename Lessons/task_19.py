# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

def reverse(start, stop):
    for i, j in zip(range(start, stop), range(stop - 1, start, -1)):
        if i >= j:
            break

        temp = some_list[i]
        some_list[i] = some_list[j]
        some_list[j] = temp


def shift(some_list):
    reverse(0, len(some_list))
    reverse(0, k)
    reverse(k, len(some_list))


some_list = [1, 2, 3, 4, 5]
k = 2

print(some_list)
shift(some_list)
print(some_list)





