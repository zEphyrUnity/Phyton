# Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

minimum = 0
maximum = 10

data = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10,
        2, 0, -9, 8, 10, -9, 0, -5, -5, 7]


def select(data_list):
    return [i for i in range(len(data_list)) if minimum < data_list[i] < maximum]


print(*select(data))
