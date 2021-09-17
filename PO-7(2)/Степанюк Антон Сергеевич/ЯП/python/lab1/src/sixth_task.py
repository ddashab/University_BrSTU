import random


def task6_1():
    n = int(input("Enter the size of your Matrix - "))
    matrix = []
    row = []
    sum_of_elements = 0
    for i in range(n):
        for j in range(n):
            row.append(random.randint(0, 10))
        matrix.append(row)
        row = []
    for row in matrix:
        sum_of_elements += sum(row)
    for row in matrix:
        print(row)
    print("The sum is", sum_of_elements)


def task6_2_1():
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Original list -", my_list)
    my_list.pop(0)
    my_list.pop(0)
    my_list.append(random.randint(1, 10))
    my_list.append(random.randint(1, 10))
    print("Modified list -", my_list)


def task6_3_1():
    groups = [["БО-331101", ["Акулова Алена", "Пабушкина Асения"]],
            ["БО-402000", ["Игорь Держатель Востока", "Солевой Голем Дмитрий"]]]
    for group in groups:
        print(group[0])
        for name in group[1]:
            print(name)


def task6_4_1():
    groups = [["БО-331101", ["Акулова Алена", "Пабушкина Асения"]],
              ["БО-402000", ["Игорь Держатель Востока", "Солевой Голем Дмитрий"]]]
    for group in groups:
        for name in group[1]:
            if name[0] == "А":
                print(group[0], name)