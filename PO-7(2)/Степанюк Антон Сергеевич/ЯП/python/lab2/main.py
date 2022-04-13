import sys
import os
from os import system, name


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def count_files():
    return len(os.listdir('C:\\Users\\bulmark\\PycharmProjects\\YapLab2'))


def read_file(filename: str):
    if not os.path.exists(filename):
        return None
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read().split('\n')


def divide_csv(filename: str):
    csv = []
    for row in read_file(filename):
        csv.append(row.split(','))
    return csv


def sort_by_age(csv: list):
    csv.sort(key=lambda student: student[2])


def write_to_file(csv: list, filename: str):
    with open(filename, 'w', encoding='utf-8') as file:
        for i in csv:
            file.write(','.join(i) + '\n')


def decrease_age_by_one(csv: list):
    for i in csv:
        i[2] = str(int(i[2]) - 1)


def print_scv(csv: list):
    for i in csv:
        print(','.join(i))


def main():
    file_path = ''
    csv = None
    while True:
        os.system('cls')
        print('1.Посчитать количество файлов в текущей директории.')
        print('2.Считать данные из CSV файла.')
        print('3.Отсортировать данные из CSV файла по возрасту.')
        print('4.Уменьшить возраст всех студентов на 1.')
        print('5.Сохранить данные в CSV файл.')
        print('6.Выход')
        user_input = int(input('Ввод: '))
        if user_input == 1:
            print('Количество файлов: ' + str(count_files()))
        elif user_input == 2:
            file_path = input('Введите путь к файлу или имя файла, находящегося в директории проекта: ')
            try:
                csv = divide_csv(file_path)
                print('Данные успешно считаны!')
                print_scv(csv)
            except:
                print('Не удаётся найти указанный файл.')
        elif user_input == 3:
            try:
                sort_by_age(csv)
                print_scv(csv)
            except:
                print('Данные не считаны.')
        elif user_input == 4:
            try:
                decrease_age_by_one(csv)
                print_scv(csv)
            except:
                print('Данные не считаны.')
        elif user_input == 5:
            if csv is None:
                print('Данные не считаны.')
            else:
                try:
                    write_to_file(csv, file_path)
                    print('Данные успешно загружены!')
                except:
                    print('Неверно введено имя файла!')
        elif user_input == 6:
            sys.exit(0)
        else:
            print('Неверный ввод!')
        input()
        clear()


if __name__ == "__main__":
    main()
