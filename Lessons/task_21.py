# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит

some_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, \
             {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

some_set = set()

# for item in some_list:
#     for value in item.values():
#         some_set.add(value)
#
# print(some_set)

some_set = set(value for item in some_list for value in item.values())

print(some_set)