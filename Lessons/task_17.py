# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

some_list = [1, 1, 2, 0, -1, 3, 4, 4]
some_dictionary = {}

for item in some_list:
    if item not in some_dictionary:
        some_dictionary[item] = item

print(len(some_dictionary))
