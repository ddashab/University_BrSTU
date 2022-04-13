import csv
import os


def f_1():
    files = os.listdir("C:/Users/danii/Desktop")
    print(f"Number of files: {len(files)}")

def age(person):
    return person[2]

def f_2():
    print("Start f_2")
    d = 'C:\\Users\\danii\\Desktop\\Univers\\students.csv'
    with open(d, "r") as file:
        lst = list(csv.reader(file))
        print("Неотсортированный список студентов: ")
        for row in lst:
            print(row)
        for i in range(3):
            lst[i] = str(lst[i]).split(';')
        lst.sort(key=age)
        print()
        print("Отсортированный список студентов(по возрасту): ")
        for i in range(len(lst)):
            print(*lst[i])
    file.close()
    return lst

def f_3():
    print("Start f_3")
    d = 'C:\\Users\\danii\\Desktop\\Univers\\students.csv'
    with open(d, "r") as file:
        lst = list(csv.reader(file))
        for i in range(3):
            lst[i] = str(lst[i]).split(';')
        for i in range(3):
            lst[i][2] =str(int(lst[i][2])-1)
        print("Список студентов: ")
        for i in range(len(lst)):
            print(*lst[i])
    file.close()
    return lst

def f_4(lst):
    print("Start f_4")
    d = 'C:\\Users\\danii\\Desktop\\Univers\\students.csv'
    with open(d, "w", newline="") as file:
        writer = csv.writer(file, lineterminator="\r")
        for row in lst:
            line = [';'.join(row)]
            writer.writerow(line)
    file.close()
    print("Данные успешно сохранены!")

if __name__ == '__main__':
    lst = []
    flag = True
    dir = 'C:\\Users\\danii\\Desktop\\Univers'
    while flag:
        print(
            "________________________________",
            "Выберите: ",
            "0 - Выход из программы",
            "1 - Узнать кол-во файлов в папке",
            "2 - Считать инф-цию из файла и отсортировать данные по возрасту",
            "3 - Считать инф-цию из файла и уменьшить возраст всех студентов на 1",
            "4 - Сохранить новые данные обратно в файл",
            sep="\n",
        )
        print("Ваш выбор: ")
        task = int(input())
        if task is 1:
            f_1(dir)
        elif task is 2:
            lst = f_2()
        elif task is 3:
            lst = f_3()
        elif task is 4:
            f_4(lst)
        elif task is 0:
            flag = False
        else:
            print("Неверный ввод! Попробуйте еще раз!")

