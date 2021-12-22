import os,csv

def task_1():
    files = os.listdir("C:")
    print ('C: содержит папки: ', files)
    print ('Количество папок: ', len(files))

def list_output(arr):
    for i in arr:
        for j in range(len(i)):
            print(i[j], end = " ")
        print()
    print()

def reader():
    f = open ("stud.csv", "r")
    reader = csv.reader(f)
    arr = []
    for i in reader:
        arr.append(str(i)[2:len(i) - 3].split(';'))
    f.close()
    print ("Исходные данные: ", arr, "\n")
    output (arr)
    return arr

def writer(arr):
    f = open ("stud.csv", "w", newline = "")
    writer = csv.writer(f)
    for i in arr:
        line = [';'.join(i)]
        writer.writerow(line)
    f.close()

def sort_col_task_2(i):
    return i[3]

def task_2():
    print ("Задание 2.")
    students = reader()

    students.sort(key = sort_col_task_2)
    print("Отсортированный список: ", students, "\n")
    
    output(students)
    writer(students)
    students.clear

def task_3():
    print ("Задание 3.")
    students = reader()
    
    num_group = input("Введите номер группы: ")
    for i in range(len(students)):
        if students[i][3] == num_group:
            students[i][2] = str(int(students[i][2]) - 1)
    print ("\nНовый список: ", students, "\n")
    
    output (students)
    writer (students)
    students.clear

def menu():
    num_task = -1
    while (num_task != 0):
        print("0 - Выход")
        print("1 - Задание 1")
        print("2 - Задание 2")
        print("3 - Задание 3\n")
        num_task = int(input("Введите номер задания: "))
        if num_task == 1:
            task_1()
        elif num_task == 2:
            task_2()
        elif num_task == 3:
            task_3()
        else:
            print("Вы ввели неправильный номер задания") 

        if (input("Хотите продолжить? (+/-)\n") == '-'):    
            break;
        print()

menu()

