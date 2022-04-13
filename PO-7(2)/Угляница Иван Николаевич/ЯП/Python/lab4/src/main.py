from string import punctuation
from copy import deepcopy

# 1 task
def task1_1():
    print("enter five numbers:")
    a, b, c, d, k = map(float, input().split())
    try:
        result = abs(
            (a ** 2 - b ** 3 - c ** 3 * a ** 2) * (b - c + c * ((k - d) / b ** 3))
            - ((k / b - k / a) * c) ** 2
            - 20000
        )
        print(result)
    except ZeroDivisionError:
        print("Something went wrong")


def task1_2():
    main_s = [1, 2, 3, 4, 5, 6]
    for i in main_s:
        if i % 2 != 0:
            print(i)


def task1_3():
    main_s_1 = [-1, 1, 2, -5, 3, 4, 10, 12]
    temp = 0
    for i in main_s_1:
        if 1 <= i <= 10:
            temp += i
    print(temp)


def task1_4():
    arr = [1, 6, 235, 7, 87, -7]
    min_el = arr[0]
    for i in arr:
        if i < min_el:
            min_el = i
    print(min_el)


# task 2
def task2_1():
    my_number = 7
    print('Enter number(7)')
    user_number = int(input())
    while user_number != my_number:
        print("Try again")
        user_number = int(input())
    if user_number == my_number:
        print("success")


def task2_2():
    big_str = ["IvanUglianitsa", "map", "hello"]
    for i in big_str:
        if len(i) < 10:
            print(i)


def task2_3():
    len_str = int(input("Enter size:"))
    print("R" * len_str)


def task2_4():
    str_sym_num = "12IH8o9P"
    new_str = ""
    for i in str_sym_num:
        if i.isalpha():
            new_str += i
    print(new_str)


matrix = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9, 7, 5, 3],
    [3, 1, 5, 3, 2, 6, 5, 7],
    [1, 7, 5, 9, 7, 3, 1, 5],
    [2, 6, 3, 5, 1, 7, 3, 2],
]
# task 3
def task3_1():
    copymatrix = deepcopy(matrix)
    print("Matrix with squares of numbers")
    for rows in range(len(copymatrix)):
        for cols in range(len(copymatrix[rows])):
            if copymatrix[rows][cols] % 2 == 0:
                copymatrix[rows][cols] *= copymatrix[rows][cols]
            print(copymatrix[rows][cols], end=" ")
        print()


def task3_2():
    copymatrix = deepcopy(matrix)
    new_matrix = []
    print("Matrix after addition(по столбцам)")
    for rows in range(len(copymatrix)):
        result = 0
        for cols in range(len(copymatrix[rows])):
            result += copymatrix[cols][rows]

        new_matrix.append(result)
    print(new_matrix)


def task3_4():
    copymatrix = deepcopy(matrix)
    res = 0
    print("Result of adding all the elements")
    for rows in range(len(copymatrix)):
        for cols in range(len(copymatrix[rows])):
            res += copymatrix[rows][cols]
    print(res)


def task3_5():
    copymatrix = deepcopy(matrix)
    replace_num = int(input("Enter number to replace"))
    for rows in range(len(copymatrix)):
        for cols in range(len(copymatrix[rows])):
            if copymatrix[rows][cols] < replace_num:
                copymatrix[rows][cols] = replace_num
            print(copymatrix[rows][cols], end=" ")
        print()


def task3_6():
    copymatrix = deepcopy(matrix)
    del_col = int(input("enter the number of the column to delete"))
    for row in range(len(copymatrix)):
        del copymatrix[row][del_col]
    print(*copymatrix, sep="\n")


###
def task3_7():
    new_matrix = []
    row = int(input("Enter row size"))
    col = int(input("Enter column size"))
    for i in range(row):
        new_matrix.append([])
        for j in range(col):
            new_matrix[i].append(0)
    print(*new_matrix, sep="\n")


def task3_8():
    row_sqrt = int(input("Enter column:"))
    row_sqrt += 1
    copymatrix = deepcopy(matrix)
    temp_list = []
    for col in range(len(copymatrix[row_sqrt])):
        temp_list.append(copymatrix[row_sqrt][col] ** 2)
    print(temp_list)


def task4_1():
    main_str = "лихо тихо , лист ."
    temp = main_str.split(" ")
    temp_end = []
    for i in range(len(temp)):
        if temp[i] not in punctuation and len(temp[i]) > 1:
            if temp[i][0] == "л" and temp[i][1] == "и":
                temp_end.append(temp[i])
    print(temp_end)


def task4_2():
    students_main = (
        "Ф;И;О;Возраст;Категория;"
        "_Иванов;Иван;Иванович;23 года;Студент 3 курса;"
        "_Петров;Семен;Игоревич;22 года;Студент 2 курса"
    )
    students_res = students_main.split(";_")
    data = []
    for row in students_res:
        data.append(row.split(";"))
    print(
        "{:1}{:1}{:31}{:20}{:20}".format(
            data[0][0], data[0][1], data[0][2], data[0][3], data[0][4]
        )
    )
    for i in data[1:]:
        print("{:7}{:6}{:20}{:20}{:20}".format(i[0], i[1], i[2], i[3], i[4]))


def task4_3():
    students = (
        "ФИО;Возраст;Категория;"
        "_Иванов Иван Иванович;23 года;Студент 3 курса;"
        "_Петров Семен Игоревич;22 года;Студент 2 курса;"
        "_Иванов Семен Игоревич;22 года;Студент 2 курса;"
        "_Акибов Ярослав Навич;23 года;Студент 3 курса;"
        "_Борков Станислав Максимович;21 год;Студент 1 курса;"
        "_Петров Семен Семенович;21 год;Студент 1 курса;"
    )
    students_new = students.split(";_")
    data_new = []
    info = []
    for row in students_new:
        data_new.append(row.split(";"))
    for i in data_new[1:]:
        if "21" in i[1]:
            info.append(i)
    for i in info:
        print(" ".join(i))


def task4_4():
    my_str = "hello my dear friends"
    print(f"Symbols: {len(my_str)}")
    print(f"Words: {len(my_str.split(' '))}")

def task6_1():
    matrix = [
        [1, 2, 3],
        [2, 4, 5]
    ]
    sum = 0
    for i in matrix:
        for j in i:
            sum += j
    print(sum)

def task6_2():
    my_list = [1, 2, 3, 5, 6, 9, 8]
    new_el = [0, 10]
    index_ = []
    for i in my_list:
        if i % 2 == 0:
            my_list.remove(i)
    for i in new_el:
        my_list.append(i)
    print(my_list)

def task6_3():
    group = [["БО-331101", ["Акулова Алена", "Пабушкина Асения"]], ["БО-402000", ["Игорь Держатель Востока", "Солевой Голем Дмитрий"]]]
    name = 'БО-331101'
    for i in group:
        if name in i[0]:
            print(f"{i[0]}:{', '.join(i[1])}")


def task6_4():
    group = [["БО-331101", ["Акула Алена", "Пабушкина Асения"]],
             ["БО-402000", ["ДержательВостока Игорь", "СолевойГолем Дмитрий"]]]
    temp = []
    for i in group:
        for j in i[1]:
            temp.append(j.split(' '))
    for i in temp:
        if len(i[0]) < 7:
            print(' '.join(i))

def main() -> None:
    print('\nЗадание 1')
    print(1.1)
    task1_1()
    print(1.2)
    task1_2()
    print(1.3)
    task1_3()
    print(1.4)
    task1_4()
    print('\nЗадание  2 «Строки и списки»')
    print('task 2.1')
    task2_1()
    print('task 2.2')
    task2_2()
    print('task 2.3')
    task2_3()
    print('task 2.4')
    task2_4()
    print('\nЗадание 3 «Матрицы»')
    print('task 3.1')
    task3_1()
    print('task 3.2')
    task3_2()
    print('task 3.4')
    task3_4()
    print('task 3.5')
    task3_5()
    print('task 3.6')
    task3_6()
    print('task 3.7')
    task3_7()
    print('task 3.8')
    task3_8()
    print('\nЗадание 4 «Строки»')
    print('task 4.1')
    task4_1()
    print('task 4.2')
    task4_2()
    print('task 4.3')
    task4_3()
    print('task 4.4')
    task4_4()
    print('\nЗадание 6 «Списки»')
    print('task 6.1')
    task6_1()
    print('task 6.2')
    task6_2()
    print('task 6.3')
    task6_3()
    print('task 6.4')
    task6_4()


if __name__ == "__main__":
    main()



