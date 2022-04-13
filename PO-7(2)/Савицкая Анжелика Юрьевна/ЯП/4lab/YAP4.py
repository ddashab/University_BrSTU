from math import *
def task_1_1():
    print ("Задание 1")

    a = int(input("Введите a: "))
    b = int(input("Введите b: "))
    c = int(input("Введите c: "))
    d = int(input("Введите d: "))
    k = int(input("Введите k: "))
    if a == 0 or b == 0 or k == 0:
       print("Дел на ноль.")
    else:
        res = fabs((a ** 2 / b ** 2 + c ** 2 / a ** 2) / (a + b + c * (k - a/(b ** 3))) + c + ((k/b - k/a)) * c)
        print("Результат: ", res)

def task_1_2():
    print ("Задание 2")
    list = ['9', 68, "fgergehdg", "jsdlw", 3, 7, 19]
    print("Cписок: ", list)
    print("Новый список: ", list[1:6:2])
    list.clear

#Дан произвольный список, содержащий только числа. Выведите результат сложения всех чисел от 1 до 10
def task_1_3(numbers):
    print ("Задание 3")
    print ("Список: ", numbers)

    sum = 0
    for i in range(len(numbers)):
        if(numbers[i] > 10):
            sum += numbers[i]
    print("Сумма: ", sum)

#Дан произвольный список, содержащий только числа. Выведите минимальное число
def task_1_4(numbers):
    print ("Задание 4")
    print("Список: ", numbers)
    print("Мин. число:", max(numbers))

#Пусть задано некоторое число my_number. Пользователь вводит с клавиатуры свое число user_number. Запрашивайте у пользователя вводить число user_numder до тех пор, пока оно не будет меньше my_number.
def task_2_1():
    print ("Задание 1")
    my_number = 19
    user_number = int(input("Введите число: "))
    while(user_number < my_number):
        user_number = int(input("Введите число (цикл остановится, когда введете число больше 10): "))

#Выведите построчно все строки размером от 5 до 10 символов.
def task_2_2():
    print ("Задание 2")
    list = ["rhrggg", "ud483fjv", "ur", "rnetymkty"]
    print("Список: ", list)
    for i in range(len(list)):
        if (len(list[i]) > 5 and len(list[i]) < 10):
            print(list[i])
    list.clear

import random
from random import choice
from string import ascii_lowercase

#Сгенерируйте и выведите случайную строку размером 5 символов, содержащую только заглавные буквы алфавита.
def task_2_3():
    print ("Задание 3")
    str =""
    for i in range(5):
        str += choice(ascii_lowercase)
        str = str.upper()
    print(str)

def task_2_4():
    print ("Задание 4")
    stroka = "dfok34384fkgv"
    print ("Исходная строка: ", stroka)    
    new_stroka = ""
    for k in range(len(stroka)):
        if (stroka[k].isdigit()):
            new_stroka += stroka[k]
    print ("Цифры: ", new_stroka)
    print()

def task_3_1(matr, size_str, size_col):
    print ("Задание 1")
    for i in range(size_str):
        for j in range(size_col):
            matr[i][j] = int(matr[i][j] ** 2)
            print(matr[i][j], end = " ")
    print()

def task_3_2(matr, size_str, size_col):
    print ("Задание 2")
    sum_str = []
    for i in range(size_str):
        for j in range(size_col):
            sum_str.append(0)
            sum_str[i] += matr[i][j]

    for i in range(size_str):
        print(sum_str[i], end =" ")
    print()

def task_3_3(matr, size_str, size_col):
    print ("Задание 3")
    for i in range(size_str):
        mult = 1
        for j in range(size_col):
            mult *= matr[i][j]          
        print(mult, end =" ")
    print()

def task_3_4(matr, size_str, size_col):
    print ("Задание 4")
    for i in range(size_str):
        for j in range(size_col):
            if matr[i][j] % 2 == 0:
                matr[i][j] = 25
            print(matr[i][j], end = ' ')
    print()

#Пусть дана строка, состоящая из слов, пробелов и знаков препинания. На основании этой строки создайте новую и выведите ее на консоль, содержащую только слова, состоящие из 5 символов.
def task_4_1():
    print ("Задание 1")
    line = input('Введите строку(слова, пробелы, знаки препинания): ')

    line = line.split( )
    newline = ''
    for i in line: 
        if len(i) < 5 :
            newline += i
            newline += ' '
    print ('Новая строка: ', newline)

def task_4_2():
    print ("Задание 2")
    str = my_string.split('_')
    
    for i in range(len(str)):
        str[i] =  str[i].split(';')
        name = str[i][0]
        surname = str[i][1]
        middlename = str[i][2]
        age = str[i][3]
        category = str[i][4]
        name_surname_middlename = name + ' ' + surname + ' ' + middlename
        print("%-36s\t%-16s\t%-12s" % (name_surname_middlename, category, age))

#Пусть дана строка произвольной длины. Выведите информацию о том, сколько в ней символов и сколько слов
def task_4_4():
    print ("Задание 4")
    print ('Результат:')
    my_string ='iduhf wieufhweifw fwfuwef efhefe fwofw efwfuhfowifbw fifhw fniwfhiw fufd fefhef eu'
    print("Строка: ", my_string) 
    print("Длина строки: ", len(my_string), "Количество слов: ", len(my_string.split()))

#Пусть дана матрица чисел размером NxN. Представьте данную матрицу в виде списка. Выведите результат сложения всех элементов матрицы
def task_5_1():
    print ("Задание 1")
    N = 5
    matr = [[1,2,3,4,5], 
            [6,7,8,9,0], 
            [2,3,4,5,6], 
            [7,8,9,0,1], 
            [1,3,6,4,9]]
    list = []
    print("Матрица: ")
    for i in range(N):
        for j in range(N):
            print(matr[i][j], end = ' ')
            list.append(matr[i][j])
        print()
    print("Список: ", list)
    sum = 0
    for i in list:
        sum += list[i]
    print("Сумма: ", sum)
    list.clear
    matr.clear

#Пусть дан список на 10 элементов. Удалите первые 2 и добавьте  2 новых. Выведите список на экран
def task_5_2():
    print ("Задание 2")
    N = 10
    list = []
    for i in range(N):
        list.append(i)
    print("Исходный список: ", list)

    list.pop(0)
    list.pop(0)
    print("Удалила первые 2 элемента: ", list)
    list.append(2233)
    list.append(9012)
    print("Добавила еще 2 элемента: ", list)
    list.clear


def menu():
    num_task = -1
    while (num_task != 0):
        print("(0) Выход")
        print("(1) Задание 1")
        print("(2) Задание 2")
        print("(3) Задание 3")
        print("(4) Задание 4")
        print("(5) Задание 5")
        num_task = int(input("Введите номер задания(от 0 до 5): "))
        if num_task == 1:
            task_1_1()
            task_1_2()
            import random
            numbers = list(random.randrange(1, 50, 1) for i in range(7))
            task_1_3(numbers)
            task_1_4(numbers)
            numbers.clear
        elif num_task == 2:
            task_2_1()
            task_2_2()
            task_2_3()
            task_2_4()
        elif num_task == 3:
            matr = [[1,2,3,4,5,6,7,8], 
            [8,7,6,5,4,3,2,1], 
            [2,3,4,5,6,7,8,9], 
            [9,8,7,6,5,3,2,1], 
            [1,3,5,7,9,7,5,3],
            [3,1,5,3,2,6,5,7],
            [1,7,5,9,7,3,1,5],
            [2,6,3,5,1,7,3,2]
            ] 
            size_str = 8
            size_col = 8
            task_3_1(matr, size_str, size_col)
            task_3_2(matr, size_str, size_col)
            task_3_3(matr, size_str, size_col)
            task_3_4(matr, size_str, size_col)
            matr.clear
        elif num_task == 4:
            task_4_1()
            task_4_2()
            task_4_4()
        elif num_task == 5:
            task_5_1()
            task_5_2()  
            my_len.clear
        else:
            print("Вы ввели неправильный номер задания") 

        if (input("Хотите продолжить? (+/-)\n") == '-'):    
            break;
menu()


