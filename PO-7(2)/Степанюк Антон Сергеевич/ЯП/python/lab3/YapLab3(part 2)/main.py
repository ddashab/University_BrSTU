
class Employee:
    count = 0
    __name = str()
    __salary = int()

    def __init__(self):
        Employee.count += 1
        print("Вызов конструктора №" + str(Employee.count))

    def __init__(self, name="", salary=0):
        Employee.count += 1
        print("Вызов конструктора №" + str(Employee.count))
        try:
            self.__name = str(name)
            self.__salary = int(salary)
        except ValueError as e:
            print(e)

    def __del__(self):
        print("Вызов деструктора №" + str(Employee.count))
        Employee.count -= 1

    def set_name(self, name):
        self.__name = name

    def set_salary(self, salary):
        self.__salary = salary

    def get_name(self):
        return self.__name

    def get_salary(self):
        return self.__salary

    def read(self):
        try:
            self.__name = str(input("Введите имя работника: "))
            self.__salary = int(input("Введите зарплату работника: "))
        except ValueError as e:
            print(e)

    def show(self):
        print("Имя: " + self.__name + " Зарплата: " + str(self.__salary))


class Actor(Employee):
    __role = str()

    def __init__(self):
        super(Actor, self).__init__()

    def __init__(self, name="", salary=0, role=""):
        super(Actor, self).__init__(name, salary)
        self.__role = role

    def set_role(self, role):
        self.__role = role

    def get_role(self):
        return self.__role

    def read(self):
        try:
            self.__name = str(input("Введите имя работника: "))
            self.__salary = int(input("Введите зарплату работника: "))
            self.__role = str(input("Введите роль: "))
        except ValueError as e:
            print(e)

    def show(self):
        print(" Имя: " + self.get_name() + " Зарплата: " + str(self.get_salary()) + " Роль: " + self.__role)


class Director(Employee):
    __films_count = int()

    def __init__(self):
        super(Director, self).__init__()

    def __init__(self, name="", salary=0, films_count=0):
        super(Director, self).__init__(name, salary)
        self.__films_count = int(films_count)

    def set_role(self, films_count):
        self.__films_count = films_count

    def get_role(self):
        return self.__films_count

    def read(self):
        try:
            self.__name = str(input("Введите имя работника: "))
            self.__salary = int(input("Введите зарплату работника: "))
            self.__films_count = int(input("Введите количество снятых фильмов: "))
        except ValueError as e:
            print(e)

    def show(self):
        print("Имя: " + self.get_name() + " Зарплата: " + str(self.get_salary()) + " Кол-во снятых фильмов: " + str(self.__films_count))


def main():
    johny = Actor()
    bill = Actor()
    lars = Director("Ларс фон Триер", 10000, 110)
    johny.read()
    bill.read()
    johny.show()
    bill.show()
    lars.show()


if __name__ == "__main__":
    main()