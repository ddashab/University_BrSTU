import random


def task2_1_1():
    my_number = 69
    while True:
        user_number = int(input('Enter ur number: '))
        if user_number > my_number:
            break


def task2_2_1():
    names = ['Anton', 'Igor', 'Ivan', 'Dmitriy', 'Gleb', 'Vova', 'Roma', 'Oleg']
    for name in names:
        if 5 < len(name) < 10:
            print(name)


def task2_3_1():
    rus_alpha = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    resault = ''
    for i in range(5):
        resault += random.choice(rus_alpha)
    print(resault)


def task2_4_1():
    string = input()
    numeric = ''
    for ch in string:
        if ch.isdigit():
            numeric += ch
    print(numeric)