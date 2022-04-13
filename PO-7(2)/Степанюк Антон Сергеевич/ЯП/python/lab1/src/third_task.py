def asign_matrix():
    return [[1, 2, 3, 4, 5, 6, 7, 8],
            [8, 7, 6, 5, 4, 3, 2, 1],
            [2, 3, 4, 5, 6, 7, 8, 9],
            [9, 8, 7, 6, 5, 4, 3, 2],
            [1, 3, 5, 7, 9, 7, 5, 3],
            [3, 1, 5, 3, 2, 6, 5, 7],
            [1, 7, 5, 9, 7, 3, 1, 5],
            [2, 6, 3, 5, 1, 7, 3, 2]]


def task3_1_1():
    matrix = asign_matrix()
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            matrix[row][column] **= 2
    print(matrix)


def task3_2_1():
    matrix = asign_matrix()
    row_sum = [0] * len(matrix)
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            row_sum[row]+= matrix[row][column]
    print(row_sum)


def task3_4_1():
    matrix = asign_matrix()
    row_sum = [1] * len(matrix)
    for row in range(len(matrix)):
        for column in range(len(matrix[row])):
            row_sum[row] *= matrix[row][column]
    print(row_sum)


def task3_5_4():
    matrix = asign_matrix()
    for i in range(4):
        matrix.pop()
    print(matrix)


def task3_6_4():
    matrix = asign_matrix()
    tmp = matrix[0]
    matrix[0] = matrix[-1]
    matrix[-1] = tmp
    print(matrix)


def task3_7_4():
    matrix = asign_matrix()
    user_number = int(input())
    user_number_count = 0
    for row in matrix:
        user_number_count += row.count(user_number)
    print(user_number_count)

