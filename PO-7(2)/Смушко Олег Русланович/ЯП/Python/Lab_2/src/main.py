def task_1():
    print('Задание 1.')
    import os
    amount_of_files = os.listdir('Directory')
    print('Количество файлов в директории:', len(amount_of_files))


def task_2_3_4_5():
    import csv
    my_list = []

    def menu():
        while True:
            while True:
                choice = int(input('Выберите, что вы хотите сделать:'
                                   '\n1 - Задание №3: уменьшить возраст студентов выбранной группы.'
                                   '\n2 - задание №4: записать данные в файл.'
                                   '\n-->'))
                if choice == 1:
                    lower_age()
                    break
                elif choice == 2:
                    write_to_csv()
                    break
                print('\nНеверный ввод. Попробуйте снова.')
            resume = str(input('Хотите продолжить? (Да / Нет): '))
            if resume.lower() == 'да':
                menu()
            elif resume.lower() == 'нет':
                print('Завершение программы...')
            break

    def write_to_csv():
        with open('Directory\\Written_file.csv', mode='w',
                  encoding='utf-8') as write_file:
            file_writer = csv.writer(write_file, lineterminator='\r')
            file_writer.writerow(['№', 'ФИО', 'Возраст', 'Группа'])
            for i in my_list:
                file_writer.writerow(i)
        print('\nДанные успешно записаны в файл.')

    def read_from_csv():
        with open('Directory\\task_2.csv',
                  encoding='utf-8') as read_file:
            file_reader = csv.reader(read_file)
            counter = 0
            for row in file_reader:
                if counter == 0:  # Печатаем шапку
                    print(f'{row[0]} {row[1]:<26}{row[2]:<11}{row[3]}')
                else:
                    my_list.append(row)
                    if int(row[2]) > 22:
                        print(f'{row[0]} {row[1]:<26}{row[2]:<11}{row[3]}')
                counter = 1
        print('Итоговый список списков:', my_list)
        return my_list

    def lower_age():
        while True:
            group = int(input('Введите группу, в которой необходимо уменьшить возраст всех студентов:'
                              '\n1 - БО-111111'
                              '\n2 - БОВ-777777'
                              '\n3 - БО-222222'
                              '\n-->'))
            if group == 1:
                name_group = 'БО-111111'
                break
            if group == 2:
                name_group = 'БОВ-777777'
                break
            if group == 3:
                name_group = 'БО-222222'
                break
            print('Неверно введено число.')
        print('Список студентов с уменьшенным возрастом.')
        print('№', 'ФИО', 'Возраст'.ljust(10), 'Группа')
        for element in my_list:
            if element[3].startswith(name_group):
                element[2] = str(int(element[2])-1)
                print(element[0], element[1].ljust(25), element[2].ljust(10), element[3])
        print('Изменённый список:', my_list)

    print('\nЗадание 2.')
    _list_ = read_from_csv()
    print('\nЗадание 3 и 4.')
    menu()


def main():
    task_1()
    task_2_3_4_5()


main()
