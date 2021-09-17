import random

matrix = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9, 7, 5, 3],
    [3, 1, 5, 3, 2, 6, 5, 7],
    [1, 7, 5, 9, 7, 3, 1, 5],
    [2, 6, 3, 5, 1, 7, 3, 2]
]


def f1():
    a, b, c = int(input("Введите значение а: ")), int(input("Введите значение b: ")), int(input("Введите значение c: "))
    if (c - a) != 0:
        print(abs(1 - a * (b ** c) - a * (b ** 2 - c ** 2) + (b - c + a) * (12 + b) / (c - a)))
    else:
        print("Деление на ноль!")


def f2():
    element = [2, 4, 6, 'a', 10, 'asd', 1]
    print(element)
    finish = ''
    for i in element:
        if isinstance(i, int) and i % 2 == 0:
            finish += f' {i} '
    print(finish)


def f3():
    element = [2, 4, 6, 87, 10, 1]
    print(element)
    finish = 1
    for i in element:
        if isinstance(i, int) and i < 10:
            finish *= i
    print(finish)


def f4():
    element = [2, 4, 6, 10, 1]
    print(element)
    finish = 0
    for i in element:
        if isinstance(i, int):
            finish += i
    print(finish / len(element))


def f5():
    my_number = 32
    print("Заданное число my_number: ", my_number)
    print("Введите число user_number:")
    user_number = int(input())
    while user_number == my_number:
        user_number = int(input("Введите новое число my_number:"))
        print("Число user_number:", user_number)


def f6():
    s = ['derfgf', 'gsdffg', 'rttrr', 'erar']
    print(s)
    for i in s:
        if i[-1] == 'r':
            print(i, end=' ')


def f7():
    s = [str(random.randint(0, 9)) for i in range(5)]
    s.insert(random.randint(0, 5), '3')
    print(' '.join(s))


def f8():
    s = input("Введите случайную строку: ")
    print(s)
    s1 = []
    for i in s:
        if i == 'л':
            s1.append(i)
    print(''.join(s1))


def f9():
    global matrix
    for i in range(len(matrix)):
        print(matrix[i])
    for i in range(8):
        for j in range(8):
            if matrix[i][j] < 5:
                matrix[i][j] = matrix[i][j] ** 2
    print()
    for i in range(len(matrix)):
        print(matrix[i])


def f10():
    for i in range(len(matrix)):
        print(matrix[i])
    for i in range(8):
        sum = 0
        for j in range(8):
            if matrix[i][j] % 2 == 0:
                sum += matrix[i][j]
        print ( 'Сумма чётных элементов в строке {}: {}'.format(i+1, sum))


def f11():
    for i in range(len(matrix)):
        print(matrix[i])
    a, b = 0, 0
    for i in range(8):
        for j in range(8):
            if matrix[i][j] < 5:
                a += matrix[i][j]
            else:
                b += matrix[i][j]
    print("Сумма элементов меньше 5: ", a)
    print("Сумма элементов больше или равно 5: ", b)
    print(max(a, b))


def f12():
    for i in range(len(matrix)):
        print(matrix[i])
    n = int(input("Номер строки для удаления от 1 до 8: "))
    if 0 < n < 9:
        del matrix[n - 1]
    else:
        print("error")
    print()
    for i in range(len(matrix)):
        print(matrix[i])


def f13():
    for i in range(len(matrix)):
        print(matrix[i])
    s1 = matrix[0]
    matrix[0] = matrix[7]
    matrix[7] = s1
    print()
    for i in range(len(matrix)):
        print(matrix[i])


def f14():
    for i in range(len(matrix)):
        print(matrix[i])
    x = int(input("номер строки: "))
    y = int(input("номер столбца: "))
    if 0 < x < 9 and 0 < y < 9:
        print("элемент: ", matrix[x - 1][y - 1])
    else:
        print("ошибка!")


def f15():
    s = "fkjkgj fgre/fg erlmtggyt? fml. dftrdrmg"
    stroka = s.split()
    print(*stroka)
    stroka_new = []
    for word in stroka:
        word_n = [w for w in word if w.isalpha()]
        if 11 > len(word_n) > 4:
            stroka_new.append(''.join(word_n))
    print(*stroka_new)


def output_data(data_1, data_2, cap):
    for i in range(int(cap) - 1):
        if i == int(cap) - 2:
            data_1[i], data_1[i + 1] = data_1[i + 1], data_1[i]
            print(data_1[i], data_1[i + 1], sep=',')
        else:
            print(data_1[i].ljust(len(max(data_1[i], data_2[i])) + 2), end='')


def f16():
    my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса'
    print(my_string)

    list_data = my_string.split(';_')
    cap = list_data[0].split(';')

    data_1 = list_data[1].split(';')
    data_2 = list_data[2].split(';')

    for i in range(len(cap) - 1):
        if i == len(cap) - 2:
            print("О студенте".center(len(data_1[i]) + len(data_1[i + 1])))
        else:
            print(cap[i].ljust(len(max(data_1[i], data_2[i])) + 2), end='')

    output_data(data_1, data_2, len(cap))
    output_data(data_2, data_1, len(cap))


def f17():
    my_string = 'ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;_Петров Семен Игоревич;22 года;' \
                'Студент 2 курса;_Иванов Семен Игоревич;22 года;Студент 2 курса;_Акибов Ярослав Наумович;' \
                '23 года;Студент 3 курса;_Борков Станислав Максимович;21 год;Студент 1 курса;_Петров Семен Семенович;' \
                '21 год;Студент 1 курса;_Романов Станислав Андреевич;23 года;Студент 3 курса;_Петров Всеволод Борисович;' \
                '21 год;Студент 2 курса'
    print(my_string)
    list_data = my_string.split(';_')

    for i in range(1, len(list_data)):
        data = list_data[i].split(';')
        if int(data[1][:3]) > 21:
            print(', '.join(data))


def f18():
    s = input().split()
    print(s)
    symbol = 0
    for i in range(len(s)):
        symbol += len(s[i])
    print("Number of characters:", symbol)
    print("Number of words:", len(s))


def f19():
    n = int(input("Введите количество строк матрицы: "))
    m = int(input("Введите количество столбцов матрицы: "))
    a = []
    for i in range(n):
        b = []
        for j in range(m):
            b.append(int(input()))
        a += b
    for i in range(len(a)):
        print(a[i])
    print("Сумма всех эдементов:", sum(a))


def f20():
    list_date = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    print(list_date)
    list_date = list_date[:3] + list_date[9:] + [input("Введите новый элемент: "), input("Введите новый элемент: ")]
    print(list_date)


def f21():
    my_len = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения']],
              ['БО-421102', ['Акулвавыаавпаова Алена', 'Бабушкина Ксения']]]
    print(my_len)
    for i in my_len:
        print(''.join(i[0]))
        for j in i[1:]:
            print(*j, sep='\n')


def f22():
    my_len = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения', 'Пабушкина Асения']],
              ['БО-421102', ['Акулвавыаавпаова Алена', 'Бабушкина Ксения']],
              ['БО-33', ['Акулова Алена', 'П Асения', 'Пабушкина Асения']]]
    print(my_len)
    for i in my_len:
        new_list = ' '.join(i[1]).split()
        for j in range(len(new_list) // 2):
            if new_list[(2 * j)][0] == 'П' and new_list[(2 * j + 1)][0] == 'А':
                print(''.join(i[0]))
                print(new_list[2 * j], new_list[2 * j + 1])


while True:
    num = int(input("Введите номер функции: "))
    if num == 0:
        break
    elif num == 1:
        f1()
    elif num == 2:
        f2()
    elif num == 3:
        f3()
    elif num == 4:
        f4()
    elif num == 5:
        f5()
    elif num == 6:
        f6()
    elif num == 7:
        f7()
    elif num == 8:
        f8()
    elif num == 9:
        f9()
    elif num == 10:
        f10()
    elif num == 11:
        f11()
    elif num == 12:
        f12()
    elif num == 13:
        f13()
    elif num == 14:
        f14()
    elif num == 15:
        f15()
    elif num == 16:
        f16()
    elif num == 17:
        f17()
    elif num == 18:
        f18()
    elif num == 19:
        f19()
    elif num == 20:
        f20()
    elif num == 21:
        f21()
    elif num == 22:
        f22()
    else:
        print('Некорректный ввод')

    y = input('Вы хотите продолжить? ')
    if y == "0" or y == 'no' or y == 'N' or y == 'нет': break
    if y == "1" or y == 'yes' or y == 'Y' or y == 'да': continue
