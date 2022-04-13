import math
import random


def part_1():
    print("Part 1\nTask 1.4")
    a, b, c, d, k, f = [int(input("Input numbers: ")) for i in range(6)]
    if a != 0:
        print(
            math.fabs(a - b * c * d ** 3 + (c ** 5 - a ** 2) / a + f ** 3 * (a - 213))
        )

    print("Task 2.4")
    listok = ["f", 8, "r", 7, 1, "t", 2]
    for i in range(0, len(listok), 2):
        print(listok[i])

    print("Task 3.4")
    arr = [5, 19, 27, 1, 2, 7, 9, 38, 8, 17]
    total = 1
    for i in range(len(arr)):
        if arr[i] < 10:
            total *= arr[i]
    print(total)

    print("Task 4.4")
    arr = [5, 19, 27, 1, 7, 777, 9, 38, 8, 17]
    for i in arr:
        if i == len(arr) // 2:
            print(arr[i])


def part_2():
    print("Part 2\nTask 1.4")
    my_number = 8
    user_number = 0
    while user_number <= my_number:
        user_number = int(input("Input number more than 8: "))

    print("Task 2.4")
    arr = [input("Input 5 sentence: ") for i in range(5)]
    for i in arr:
        if i[0] == "r":
            print(i)

    print("Task 3.4")
    digits = "123456789"
    letters_small = "qwertyuiopasdfghjklzxcvbnm"
    letters_big = "QWERTYUIOPASDFGHJKLZXCVBNM"
    all_symbols = digits + letters_small + letters_big
    answer = "" + random.choice(digits)
    for i in range(7):
        answer += random.choice(all_symbols)
    print(answer)

    print("Task 4.4")
    my_string = input("Input string with numbers and letters: ")
    digits = ""
    letters = ""
    for i in my_string:
        if i.isdigit():
            digits += i
        else:
            letters += i
    print(f"Digits: {digits}")
    print(f"Letters: {letters}")


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


def task3_1_4():
    print("Part 3\n Task 1.4")
    for i in range(4):
        for j in range(8):
            matrix[i][j] *= matrix[i][j]
    print(matrix)


def task3_2_4():
    print("Task 2.4")
    summ = []
    for row in range(len(matrix)):
        result = 0
        for col in range(len(matrix[row])):
            if matrix[col][row] % 2 == 0:
                result += matrix[col][row]
        summ.append(result)
    print(summ)


def task3_4_4():
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            matrix[row][col] *= 0
            print(matrix[row][col])
        print()


def task3_5_3():
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 5:
                matrix[row][col] *= matrix[row][col]
    print(matrix)


def task3_6_3():
    for row in matrix:
        for col in row:
            matrix.pop()
    print(matrix)


def task3_7_3():
    counter = 0
    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            if matrix[row][col] == 3:
                counter += 1
    print(counter)


def task4_1_4():
    sentence = input("Input your string bro <3: ")
    new_sentence = ""
    for i in sentence.split(" "):
        if i.isalpha():
            new_sentence += i + "ов "
    print(new_sentence)


def task4_2_4():
    infornmation = (
        "ФИО;О студенте;"
        "_Иванов Иван Иванович;23 года Студент 3 курса;"
        "_Петров Семен Игоревич;22 года Студент 2 курса"
    )
    for i in infornmation.split(";_"):
        for g in i.split(";"):
            print("{:<25} ".format(g), end="")
        print()
        print(end="{:<3}".format("   "))


def task4_3_4():
    information = (
        "ФИО;Возраст;Категория;"
        "_Иванов Иван Иванович;23 года;Студент 3 курса;"
        "_Петров Семен Игоревич;22 года;Студент 2 курса;"
        "_Иванов Семен Игоревич;22 года;Студент 2 курса;"
        "_Акибов Ярослав Навич;23 года;Студент 3 курса;"
        "_Борков Станислав Максимович;21 год;Студент 1 курса;"
        "_Петров Семен Семенович;21 год;Студент 1 курса"
    )
    for i in information.split(";_"):
        for g in i.split(";"):
            if g[0] == "А" or g[0] == "Б":
                print(i.split(";"))


def task4_4_4():
    your_string = input("Input your string: ")
    print(f"Number of symbols: {len(your_string)}")
    print(f"Number of words: {len(your_string.split())}")


def task6_1():
    arr = [[1, 7, 2, 6], [9, 4, 3, 5], [5, 8, 8, 1], [3, 7, 2, 8]]
    summ = 0
    for i in arr:
        for j in i:
            summ += j
    print(summ)


def task6_2_4():
    my_list = ["6", "1", "leg", "car", "set", "main", "5", "7", "book", "apple"]
    new_elem = ["stone", "nike", "shop", "adidas", "food"]
    for i in new_elem:
        my_list.append(i)
    print(my_list)
    del my_list[1::2]
    print(my_list)


def task6_3_4():
    students = [
        ["БО-331101", ["Акулова Алена", "Пабушкина Асения"]],
        ["БОВ-421102", ["Сырный Пуддинг", "Дима Якимчик"]],
    ]
    for i in students:
        if "БО" in i[0]:
            print(i)


def task6_4_4():
    my_len = [["БО-331101", ["Акулова Алена", "Пабушкина Асения", "Мыльный Гном", "Модный Олег"], ],
              ["БОВ-421102", ["Сырный Пуддинг","Дима Якимчик", "Вощук Александр", "Энергетический Егор", ], ], ]
    for i in my_len:
        print(i[1][1::2])


def main():
    part_1()
    part_2()
    task3_1_4()
    task3_2_4()
    task3_4_4()
    task3_5_3()
    task3_6_3()
    task3_7_3()
    task4_1_4()
    task4_2_4()
    task4_3_4()
    task4_4_4()
    task6_1()
    task6_2_4()
    task6_3_4()
    task6_4_4()


if __name__ == "__main__":
    main()
