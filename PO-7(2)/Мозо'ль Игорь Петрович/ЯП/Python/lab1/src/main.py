import random
from pprint import pprint

print("1.1.1")


def calculation(a, b, c, d, k):
    try:
        return abs(
            (a ** 2 / b ** 2 + c ** 2 * a ** 2) / (a + b + c * (k - a / b ** 3))
            + c
            + (k / b - k / a) * c
        )
    except ArithmeticError:
        print("Error(DivisionZero)")


a, b, c, d, k = [float(input("Введите коэффициенты a,b,c,d,k")) for i in range(5)]
if (result := calculation(a, b, c, d, k)) is not None:
    print(result)

input("Нажмите любую клавишу")

print("1.2.1")
arr = [521, "fabfab", "4314614", 15315.2521, "4g3wgfw", 211244, "afqfqfq"]
for i in range(1, len(arr), 2):
    print(arr[i])

input("Нажмите любую клавишу")

print("1.3.1")
arr = [521, 0, -52151, 15315.2521, 27, 211244, -3]
sum = 0
for i in arr:
    if i > 10:
        sum += i
print(sum)

input("Нажмите любую клавишу")

print("1.4.1")
arr = [521, 0, -52151, 15315.2521, 27, 211244, -3]
max = arr[0]
for i in arr[1:]:
    if i > max:
        max = i
print(max)  # ну или просто использовать print(max(arr))

input("Нажмите любую клавишу")

print("2.1.1")
my_numb = 19
user_numb = float(input("Input number"))
while my_numb < user_numb:
    user_numb = float(input())

input("Нажмите любую клавишу")

print("2.2.1")
arr = ["521", "fabfab", "4314614", "15315.2521", "4g3wgfw", "211244", "afqfqfq"]
for i in arr:
    if 5 <= len(i) <= 10:
        print(i)

input("Нажмите любую клавишу")

print("2.3.1")
ru_uppercase = "АБВГДЕЁЖЗИЙКЛМНОПРСТФХЦЧШЩЭЮЯ"
random_string = "".join(random.choice(ru_uppercase) for i in range(5))
print(random_string)

print("2.4.1")
str = input()
str_end = "sdfsf"
for i in str:
    if i.isdigit() == True:
        str_end += i
print(str_end)

input("Нажмите любую клавишу")

print("3.1.1")


def func(arr):
    for i in range(8):
        for j in range(8):
            arr[i][j] *= arr[i][j]
    return arr


arr = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9, 7, 5, 3],
    [3, 1, 5, 3, 2, 6, 5, 7],
    [1, 7, 5, 9, 7, 3, 1, 5],
    [2, 6, 3, 5, 1, 7, 3, 2],
]

pprint(func(arr))

input("Нажмите любую клавишу")

print("3.2.1")
arr = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9, 7, 5, 3],
    [3, 1, 5, 3, 2, 6, 5, 7],
    [1, 7, 5, 9, 7, 3, 1, 5],
    [2, 6, 3, 5, 1, 7, 3, 2],
]


def sum_strings(arr):
    arr_end = []
    string_helper = 0
    for i in range(8):
        for j in range(8):
            string_helper += arr[i][j]
        arr_end.append(string_helper)
        string_helper = 0
    return arr_end


print(sum_strings(arr))

input("Нажмите любую клавишу")

print("3.4.1")
arr = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9, 7, 5, 3],
    [3, 1, 5, 3, 2, 6, 5, 7],
    [1, 7, 5, 9, 7, 3, 1, 5],
    [2, 6, 3, 5, 1, 7, 3, 2],
]


def multiplication_strings(arr):
    arr_end = []
    string_helper = 1
    for i in range(8):
        for j in range(8):
            string_helper *= arr[i][j]
        arr_end.append(string_helper)
        string_helper = 1
    return arr_end


print(multiplication_strings(arr))

input("Нажмите любую клавишу")

print("3.5.1")


def change_even_to_zero(arr):
    for i in range(8):
        for j in range(1, 8, 2):
            arr[i][j] = 0
    return arr


pprint(change_even_to_zero(arr))

input("Нажмите любую клавишу")

print("3.6.1")


def delete(arr):
    dele = int(input("Input number of deleting string"))
    if dele > 0 and dele < 9:
        arr.pop(dele - 1)
        return arr
    else:
        return None


arr = [
    [1, 2, 3, 4, 5, 6, 7, 8],
    [8, 7, 6, 5, 4, 3, 2, 1],
    [2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2],
    [1, 3, 5, 7, 9, 7, 5, 3],
    [3, 1, 5, 3, 2, 6, 5, 7],
    [1, 7, 5, 9, 7, 3, 1, 5],
    [2, 6, 3, 5, 1, 7, 3, 2],
]

if delete(arr) is not None:
    pprint(arr)
else:
    print("Wrong number")

input("Нажмите любую клавишу")

print("3.7.1")


def swap_first_last(arr):
    last_string = arr.pop()
    arr.append(arr.pop(0))
    arr.insert(0, last_string)
    return pprint(arr)


swap_first_last(arr)

input("Нажмите любую клавишу")

print("3.8.1")


def search(arr):
    i = int(input("Input number of string")) - 1
    j = int(input("Input number of columt")) - 1
    if 0 <= i <= 7 and 0 <= j <= 7:
        return arr[i][j]
    else:
        return None


if (result := search(arr)) is not None:
    print(result)
else:
    print("Wrong input")

input("Нажмите любую клавишу")

print("4.1.1")
from string import punctuation

str_begin = "Helloaf, vfavfa. dadf dadfq"
str_sup = ""
str_end = ""
counter = 1
for i in str_begin:
    if i not in punctuation and i != " ":
        str_sup += i
        if counter == len(str_begin) and len(str_sup) >= 5:
            str_end += str_sup
    elif len(str_sup) >= 5:
        str_end += str_sup + " "
        str_sup = ""
    else:
        str_sup = ""
    counter += 1
print(str_end)

input("Нажмите любую клавишу")

print("4.2.1")
my_string = (
    "Ф;И;О;Возраст;Категория;"
    "_Иванов;Иван;Иванович;23 года;Студент 3 курса;"
    "_Петров;Семен;Игоревич;22 года;Студент 2 курса"
)
student = my_string.split(";_")
word = []
for i in student:
    word.append(i.split(";"))
for i in word:
    print("{:10}{:10}{:10}{:20}{:10}".format(i[0], i[1], i[2], i[4], i[3]))

input("Нажмите любую клавишу")

print("4.3.1")
stud = (
    "ФИО;Возраст;Категория;"
    "_Иванов Иван Иванович;23 года;Студент 3 курса;"
    "_Петров Семен Игоревич;22 года;Студент 2 курса;"
    "_Иванов Семен Игоревич;22 года;Студент 2 курса;"
    "_Акибов Ярослав Навич;23 года;Студент 3 курса;"
    "_Борков Станислав Максимович;21 год;Студент 1 курса;"
    "_Петров Семен Семенович;21 год;Студент 1 курса;"
)
string = stud.split(";_")
info = []
for i in string:
    info.append(i.split(";"))
fio = []
for i in info:
    fio.append(i[0].split())
for i in range(1, len(info)):
    if fio[i][0] == "Петров":
        print(" ".join(info[i]))

input("Нажмите любую клавишу")

print("4.4.1")
string = input("Input string:")
print("Number of words=", len(string.split()), "Number of sybmols=", len(string))

input("Нажмите любую клавишу")

print("6.1.1")
arr = [[9, 7, 5, 3], [1, 3, 5, 7], [2, 4, 6, 8], [8, 6, 4, 2]]
summa = 0
new_list = []
for i in arr:
    for j in i:
        new_list.append(j)
        summa += j
print(summa)

input("Нажмите любую клавишу")

print("6.2.1")
arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = arr[2:]
for i in range(2):
    arr.append(input("Input 2 numbers or strings :"))
print(arr)

input("Нажмите любую клавишу")

print("6.3.1")
my_len = [
    ["БО-331101", ["Акулова Алена", "Бабушкина Асения"]],
    ["БОВ-421102", ["Абобус Николай", "Дмитрук Алина"]],
    ["БО-331103", ["Иванова Мария", "Коробкин Илья"]],
]
search_group = input("Input searching group")
for i in my_len:
    if search_group == i[0]:
        print("{}\n{}\n{}\n".format(i[0], i[1][0], i[1][1]))

input("Нажмите любую клавишу")

print("6.4")
my_len = [
    ["БО-331101", ["Акулова Алена", "Бабушкина Асения"]],
    ["БОВ-421102", ["Абобус Николай", "Дмитрук Алина"]],
    ["БО-331103", ["Иванова Мария", "Коробкин Илья"]],
]
for i in my_len:
    for j in i[1]:
        if j.split()[0][0] == "А":
            print("{}\t{}".format(i[0], j))
