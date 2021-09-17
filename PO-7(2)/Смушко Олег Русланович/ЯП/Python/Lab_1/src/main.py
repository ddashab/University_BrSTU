def task_1():
    def task_1_1():
        print('Задание 1.1')
        a = float(input('Введите a: '))
        b = float(input('Введите b: '))
        c = float(input('Введите c: '))
        d = float(input('Введите d: '))
        f = float(input('Введите f: '))

        if a != 0:
            result = float(a-b*c*(d**3)+(c**5 - a**2)/a + (f**3)*(a-213))
            if result < 0:
                result = -result
            print(round(result, 2))
        else:
            print('a = 0. Делить на ноль нельзя!')

    def task_1_2():
        print('\nЗадание 1.2')
        elements = [3, 56, 'Love', 4.21, 6, 'your', 'today', 67, 5.789]
        i = 1
        new_list = []
        while i < len(elements):
            new_list.append(elements[i])
            i += 2
        print('Исходный список:', elements)
        print('Новый список, состоящий из нечётных элементов: ', new_list)

    def task_1_3():
        print('\nЗадание 1.3')
        elements = [3, 6, 11, 56, 90, 5, 1, 9, 2]
        result = 1
        for i in elements:
            if i < 10:
                result *= i
        print('Исходный список:', elements)
        print('Произведение всех чисел меньше 10:', result)

    def task_1_4():
        print('\nЗадание 1.4')
        list_size = int(input('Ведите размер списка: '))
        elements = [int(input(f'Введите {i+1}-й элемент списка: ')) for i in range(list_size)]
        middle = int((len(elements)/2))
        if list_size % 2 == 0:
            print(f'Элемент посередине массива: {elements[middle-1]} или {elements[middle]}')
        else:
            print('Элемент посередине массива: ', elements[middle])
    task_1_1()
    task_1_2()
    task_1_3()
    task_1_4()


def task_2():
    def task_2_1():
        print('Задание 2.1')
        my_number = 5
        user_number = int(input('Введите значение user_number: '))
        if user_number <= 5:
            while user_number <= my_number:
                user_number = int(input('Введите новое значение: '))
        print(f'Ваше число больше {my_number}!')

    def task_2_2():
        print('\nЗадание 2.2')
        my_strings = ['reverse', 'weather', 'joke', 'robot', 'castle', 'result']
        result_string = []
        for i in my_strings:
            if i.startswith('r'):
                result_string.append(i)
        print('Исходные данные:', my_strings)
        print('Result: ', result_string)

    def task_2_3():
        print('\nЗадание 2.3')
        import random
        import string
        length = 8
        letters = string.ascii_letters
        digits = string.digits
        rand_string = ''.join(random.choice(letters + digits) for _ in range(length))
        print(rand_string)

    def task_2_4():
        print('\nЗадание 2.4')
        main_string = 'I lo23ve pom4egr89anate2 very89 mu09ch5'
        letters = ''
        digits = ''
        for i in main_string:
            if i.isdigit():
                digits += i
            else:
                if i.isalpha():
                    letters += i
        print('Исходные данные:', main_string)
        print('Digits:', digits)
        print('Letters:', letters)
    task_2_1()
    task_2_2()
    task_2_3()
    task_2_4()


def task_3():
    def task_3_1():
        print('Задание 3.1')
        from pprint import pprint
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [2, 3, 4, 5, 6, 7, 8, 9],
                  [9, 8, 7, 6, 5, 4, 3, 2],
                  [1, 3, 5, 7, 9, 7, 5, 3],
                  [3, 1, 5, 3, 2, 6, 5, 7],
                  [1, 7, 5, 9, 7, 3, 1, 5],
                  [2, 6, 3, 5, 1, 7, 3, 2]]
        lines = 4
        for i in range(lines):
            for j in range(8):
                matrix[i][j] = matrix[i][j] ** 2
        pprint(matrix)

    def task_3_2():
        print('\nЗадание 3.2')
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [2, 3, 4, 5, 6, 7, 8, 9],
                  [9, 8, 7, 6, 5, 4, 3, 2],
                  [1, 3, 5, 7, 9, 7, 5, 3],
                  [3, 1, 5, 3, 2, 6, 5, 7],
                  [1, 7, 5, 9, 7, 3, 1, 5],
                  [2, 6, 3, 5, 1, 7, 3, 2]]
        result_list = []
        for j in range(1, 8, 2):
            res_sum = 0
            for i in range(8):
                res_sum += matrix[i][j]
            if res_sum != 0:
                result_list.append(res_sum)
        print(result_list)

    def task_3_3():
        print('\nЗадание 3.3')
        from pprint import pprint
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [2, 3, 4, 5, 6, 7, 8, 9],
                  [9, 8, 7, 6, 5, 4, 3, 2],
                  [1, 3, 5, 7, 9, 7, 5, 3],
                  [3, 1, 5, 3, 2, 6, 5, 7],
                  [1, 7, 5, 9, 7, 3, 1, 5],
                  [2, 6, 3, 5, 1, 7, 3, 2]]
        for i in range(8):
            for j in range(8):
                matrix[i][j] = 0
        pprint(matrix)

    def task_3_4():
        print('\nЗадание 3.4')
        from pprint import pprint
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [2, 3, 4, 5, 6, 7, 8, 9],
                  [9, 8, 7, 6, 5, 4, 3, 2],
                  [1, 3, 5, 7, 9, 7, 5, 3],
                  [3, 1, 5, 3, 2, 6, 5, 7],
                  [1, 7, 5, 9, 7, 3, 1, 5],
                  [2, 6, 3, 5, 1, 7, 3, 2]]
        for i in range(4):
            matrix.pop()
        pprint(matrix)

    def task_3_5():
        print('\nЗадание 3.5')
        from pprint import pprint
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [2, 3, 4, 5, 6, 7, 8, 9],
                  [9, 8, 7, 6, 5, 4, 3, 2],
                  [1, 3, 5, 7, 9, 7, 5, 3],
                  [3, 1, 5, 3, 2, 6, 5, 7],
                  [1, 7, 5, 9, 7, 3, 1, 5],
                  [2, 6, 3, 5, 1, 7, 3, 2]]
        row_for_delete = int(input('Введите строку для удаления:'))
        matrix.pop(row_for_delete-1)
        pprint(matrix)

    def task_3_6():
        print('\nЗадание 3.6')
        from pprint import pprint
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [2, 3, 4, 5, 6, 7, 8, 9],
                  [9, 8, 7, 6, 5, 4, 3, 2],
                  [1, 3, 5, 7, 9, 7, 5, 3],
                  [3, 1, 5, 3, 2, 6, 5, 7],
                  [1, 7, 5, 9, 7, 3, 1, 5],
                  [2, 6, 3, 5, 1, 7, 3, 2]]
        for j in range(8):
            temp_value = matrix[0][j]
            matrix[0][j] = matrix[7][j]
            matrix[7][j] = temp_value
        pprint(matrix)

    def task_3_7():
        print('\nЗадание 3.7')
        matrix = [[1, 2, 3, 4, 5, 6, 7, 8],
                  [8, 7, 6, 5, 4, 3, 2, 1],
                  [2, 3, 4, 5, 6, 7, 8, 9],
                  [9, 8, 7, 6, 5, 4, 3, 2],
                  [1, 3, 5, 7, 9, 7, 5, 3],
                  [3, 1, 5, 3, 2, 6, 5, 7],
                  [1, 7, 5, 9, 7, 3, 1, 5],
                  [2, 6, 3, 5, 1, 7, 3, 2]]
        user_row = int(input('Введите строку для поиска: '))
        user_column = int(input('Введите столбец для поиска: '))
        if user_column > 8 or user_row > 8:
            print('Ничего не найдено. Такого элемента нет.')
        else:
            print('Элемент найден - ', matrix[user_row-1][user_column-1])
    task_3_1()
    task_3_2()
    task_3_3()
    task_3_4()
    task_3_5()
    task_3_6()
    task_3_7()


def task_4():
    def task_4_1():
        print('Задание 4.1')
        import re
        test_string = 'Петров и Иванов, а еще Игоренко собрались поехать во Львов!'
        split_string = re.split(' |,|!', test_string)
        result_string = ''
        for i in split_string:
            if i.find('ов') != -1:
                result_string = result_string + i + ' '
        print('Исходные данные:', test_string)
        print(result_string)

    def task_4_2():
        print('\nЗадание 4.2')
        my_string = 'Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;' \
                    '_Петров;Семен;Игоревич;22 года;Студент 2 курса'
        my_list = [str_.split(';') for i, str_ in enumerate(my_string.split('_')) if i > 0]
        print('{:<25}{}'.format('ФИО', 'О студенте'))
        for element in my_list:
            print(f'{element[0]} {element[1]} {element[2]:<13}{element[4]}, {element[3]}')

    def task_4_3():
        print('\nЗадание 4.3')
        my_string = 'ФИО;Возраст;Категория;_Иванов Иван Иванович;23 года;Студент 3 курса;' \
                    '_Петров Семен Игоревич;22 года;Студент 2 курса;_Иванов Семен Игоревич;22 года; Студент 2 курса;' \
                    '_Акибов Ярослав Наумович;23 года;Студент 3 курса;' \
                    '_Борков Станислав Максимович;21 год;Студент 1 курса;' \
                    '_Петров Семен Семенович;21 год;Студент 1 курса;' \
                    '_Романов Станислав Андреевич;23 года;Студент 3 курса' \
                    '_Петров Всеволод Борисович;21 год;Студент 2 курса'
        my_list = [str_.split(';') for i, str_ in enumerate(my_string.split('_')) if i > 0]
        print('{:<32}{:<11}{}'.format('ФИО', 'Возраст', 'Категория'))
        for element in my_list:
            if element[0].startswith('А') or element[0].startswith('Б'):
                print(f'{element[0]:<32}{element[1]:<11}{element[2]}')

    def task_4_4():
        print('\nЗадание 4.4')
        import string
        my_string, count = 'I love friday and clouds very much you', 0
        for i in my_string:
            if string.ascii_letters.find(i) != -1:
                count += 1
        amount_words = len(my_string.split(' '))
        print('Ваша строка:', my_string)
        print('Количество символов в строке:', count)
        print('Количество слов в строке:', amount_words)
    task_4_1()
    task_4_2()
    task_4_3()
    task_4_4()


def task_5():
    import random

    def task_5_1():
        print('Задание 5.1')

        def print_matrix(matrix):
            for i in range(size):
                for j in range(size):
                    print('{:3d}'.format(matrix[i][j]), end=' ')
                print()

        size = int(input('Введите размерность матрицы (N): '))
        matrix = []
        my_list = []
        for i in range(0, size):
            matrix.append([])
            for j in range(0, size):
                matrix[i].append(random.randint(0, 10))
                my_list.append(matrix[i][j])
        summ = 0
        for k in my_list:
            summ += k
        print_matrix(matrix)
        print('Список из матрицы:', my_list)
        print('Результат сложения всех элементов матрицы:', summ)

    def task_5_2():
        print('\nЗадание 5.2')
        my_list = []
        for j in range(10):
            my_list.append(random.randint(0, 50))
        print('Исходный список:', my_list)
        for i in range(5):
            my_list.append(int(input('Введите новый элемент списка: ')))
        print('Список после добавления новых элементов:', my_list)
        result_string = []
        for element in my_list:
            if element % 2 == 1:
                result_string.append(element)
        print('Итоговый список, состоящий из нечётных элементов:', result_string)

    def task_5_3():
        print('\nЗадание 5.3')
        my_len = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения']],
                  ['БОВ-421102', ['Кузьмин Артём', 'Прокофьев Максим']],
                  ['БО-331103', ['Тарасов Иван', 'Егоров Герман']]]
        print('{:<18}{:<16}{}'.format('Название группы', 'ФИО', 'ФИО'))
        for element in my_len:
            if element[0].startswith('БО-'):
                print(f'{element[0]:<18}{element[1][0]:<16}{element[1][1]}')

    def task_5_4():
        print('\nЗадание 5.4')
        my_len = [['БО-331101', ['Акулова Алена', 'Бабушкина Ксения', 'Баженов Максим', 'Лапина Мелания']],
                  ['БОВ-421102', ['Кузьмин Артём', 'Прокофьев Максим', 'Тарасов Алексей', 'Грачев Александр']],
                  ['БО-331103', ['Тарасов Иван', 'Егоров Герман', 'Румянцев Матвей', 'Архипов Тимофей']]]
        print('{:<19}{}'.format('Студент', 'Группа'))
        for groups in my_len:
            for counter, student in enumerate(groups[1]):
                if counter % 2 == 1:
                    print('{:<19}{}'.format(student, groups[0]))
    task_5_1()
    task_5_2()
    task_5_3()
    task_5_4()


def main():
    def menu() -> str:
        choice_ = str(input('Введите номер задания, которое хотите выполнить:'
                            '\n1 - №1'
                            '\n2 - №2'
                            '\n3 - №3'
                            '\n4 - №4'
                            '\n5 - №5'
                            '\nДля выхода нажмите "t"'
                            '\n-->'))
        return choice_
    while True:
        choice = menu()
        if choice == '1':
            task_1()
            choice = menu()
        if choice == '2':
            task_2()
            choice = menu()
        if choice == '3':
            task_3()
            choice = menu()
        if choice == '4':
            task_4()
            choice = menu()
        if choice == '5':
            task_5()
            choice = menu()
        if choice.lower() == 't':
            print('Заверешние программы...')
            break


if __name__ == '__main__':
    main()
