# Хакер Василий получил доступ к классному журналу и
# хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая
# заменяет оценки Василия, но наоборот: все
# максимальные – на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

vasya_grades = [1, 2, 5, 4, 2]

max_grade = max(vasya_grades)
min_grade = min(vasya_grades)

res = []

for el in vasya_grades:
    if el == max_grade:
        res.append(min_grade)
    else:
        res.append(el)

print(*res)


def vasya_punishment(lst, res=[], min_grade=min(vasya_grades), max_grade=max(vasya_grades)):
    if len(lst) == 0:
        return res

    if lst[0] == max_grade:
        res.append(min_grade)
    else:
        res.append(lst[0])

    return vasya_punishment(lst[1:])


print(*vasya_punishment(vasya_grades))