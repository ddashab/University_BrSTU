import os


def read_from_file(filename):# Чтение информации из файла
    listok = []
    with open(filename, "r", encoding="utf-8") as file:
        for elem in file:
            for i in elem.split('\n'):
                if i != '':
                    listok.append(i.split(';'))
        return listok


def create_array(filename, arr):# Создание массива из информации из файла
    for elem in read_from_file(filename):
        arr.append(elem)
        if elem[2].isdigit() and int(elem[2]) > 22:
            print(elem)


def write_in_file(filename, arr):# Запись информациии в файл
    with open(filename, 'w', encoding='utf-8') as file:
        for i in arr:
            file.write(';'.join(i))
            if i != arr[-1]:
                file.write('\n')


def task_1():# Колличество папок в файле
    print('Size of directory is: {}'.format(len(os.listdir())))


def task_3(arr):# Увеличение возвраста на 1
    for i in arr:
        if i[2].isdigit():
            i[2] = str(int(i[2]) + 1)


def main():
    file = "students.csv"
    information = []
    while True:
        print('1.Количество файлов \n2.Вывод информации из файла >22 \n3.Умееньшение возраста')
        print('4.Сохранение данных в файл')
        choose = int(input('Choose task: '))
        if choose == 1:
            task_1()
        elif choose == 2:
            create_array(file, information)
        elif choose == 3:
            task_3(information)
        elif choose == 4:
            write_in_file(file, information)
        else:
            print('By my friend <3')
            break


if __name__ == "__main__":
    main()
