import random


def task1_2_1():
    lst_len = int(input("Enter the number of list's elements: "))
    lst = []
    for i in range(lst_len):
        print('lst[', i, '] = ', sep='', end='')
        lst.append(input())
    for element in lst:
        if element.isdigit() and float(element) % 2 == 0:
            print(element)


def task1_3_1():
    lst_len = int(input("Enter the number of list's elements: "))
    # the sum of elements which are bigger than 10
    total = 0
    lst = []
    for i in range(lst_len):
        lst.append(random.randint(0, 50))
    print(lst)
    for element in lst:
        if element > 10:
            total += element
    print('The sum is', total)
    # 4.1


def task1_3_2():
    lst = []
    for i in range(10):
        lst.append(random.randint(0, 50))
    print(lst)
    print('The max is ', max(lst))

