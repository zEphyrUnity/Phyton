# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например,
# у операции умножения.
#
# *Пример:*
#
# **Ввод:** `print_operation_table(lambda x, y: x * y) `
# **Вывод:**
# 1 2 3 4 5 6
#
# 2 4 6 8 10 12
# 3 6 9 12 15 18
# 4 8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36

def get_multitable(rows=6, cols=6):
    col = []

    for i in range(1, rows + 1):
        row = []
        for j in range(1, cols + 1):
            row.append(i * j)
        col.append(row)

    return col


def take_element(matrix, row, col):
    return matrix[row - 1][col - 1]


def take_element2(matrix, row, col):
    return matrix[row - 1][col - 1] / 2


def print_operation_table(operation, num_rows=6, num_columns=6):
    matrix = get_multitable(11, 11)

    for i in range(num_rows):
        for j in range(num_columns):
            print(matrix[i][j], end=" ")
        print()

    print(operation(matrix, num_rows, num_columns))


print_operation_table(take_element, 6, 6)
print_operation_table(take_element2, 6, 6)
