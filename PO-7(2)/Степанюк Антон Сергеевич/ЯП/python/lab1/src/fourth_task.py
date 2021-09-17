def task4_1_1():
    string = input()
    words = string.split()
    for word in words:
        if len(word) < 5:
            words.remove(word)
    new_string = ' '.join(words)
    print(new_string)


def task4_2_1():
    my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;" \
                "_Петров;Семен;Игоревич;22 года;Студент 2 курса"
    rows = my_string.split(';_')
    s_rows = []
    for row in rows:
        s_rows.append(row.split(";"))
    print("{:1}{:1}{:31}{:20}{:20}".format(
        s_rows[0][0], s_rows[0][1], s_rows[0][2], s_rows[0][4], s_rows[0][3]))
    for row in s_rows[1:]:
        print("{:7}{:6}{:20}{:20}{:20}".format(
             row[0], row[1], row[2], row[4], row[3]))


def task4_3_1():
    my_string = "ФИО;Возраст;Категория;"\
                "_Иванов Иван Иванович;23 года;Студент 3 курса;"\
                "_Петров Семен Игоревич;22 года;Студент 2 курса;"\
                "_Иванов Семен Игоревич;22 года;Студент 2 курса;"\
                "_Акибов Ярослав Навич;23 года;Студент 3 курса;"\
                "_Борков Станислав Максимович;21 год;Студент 1 курса;"\
                "_Петров Семен Семенович;21 год;Студент 1 курса;"
    rows = my_string.split(";_")
    s_rows = []
    for row in rows:
        s_rows.append(row.split(";"))
    print("{:30}{:20}{:20}".format(s_rows[0][0], s_rows[0][1], s_rows[0][2]))
    for row in s_rows[1:]:
        # Метод find() возвращает -1, если подстрока не найдена
        if row[0].find("Петров") != -1:
            print("{:30}{:20}{:20}".format(row[0], row[1], row[2]))


def task4_4():
    my_string = input()
    print(len(my_string), "- symbols")
    words = my_string.split(" ")
    print(len(words, "- words"))


