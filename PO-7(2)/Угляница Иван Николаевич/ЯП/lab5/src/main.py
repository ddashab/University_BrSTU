import os



def read_data_from_csv(filename):  # task 5
    with open(filename, "r", encoding="utf-8") as file:
        data_r = file.read().split("\n")
        data_r.pop(-1)  # В конце списка вылезает пустой элемент и программа херится, поэтому удаляю его
        data_r.pop(0)
    return data_r


def write_data_to_file(filename, data):  # task5
    with open(filename, "a", encoding="utf-8") as file_w:
        file_w.write("№;ФИО;Возраст;Группа\n")
        for i in data:
            file_w.write(f'{";".join(i)}\n')


def task_3_raise_age(data):
    group = input("Enter group")
    for el in data:
        if el[3] == group:
            el[2] = str(int(el[2]) + 1)
    choice_wr = int(
        input("If you want write your list in file enter 1,else any other number:")
    )
    if choice_wr == 1:
        write_data_to_file('test.csv', data)


def task_1():
    files = os.listdir("./files")
    print(f"Number of files: {len(files)}")


def task_2():
    data = []
    for i in read_data_from_csv('test.csv'):
        data.append(i.split(";"))
    data = sorted(data, key=lambda el: el[2])
    print(f"Sorted list:{data}")
    choice = int(input("If you want change age enter 1,else any other number:"))
    if choice == 1:
        task_3_raise_age(data)
    else:
        print("End of the program")


if __name__ == "__main__":
    task_2()
