# Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# # 5

from bisect import bisect_left

list_1 = [1, 12, 6, 7, 8, 15]
k = 11

list_1.sort()


def take_close_number(list_, number):
    position = bisect_left(list_1, k)

    if position == 0:
        return list_[0]

    if position == len(list_):
        return list_[-1]

    next_ = list_[position]
    previous = list_[position - 1]

    if next_ - number < number - previous:
        return next_
    else:
        return previous


print(take_close_number(list_1, k))

