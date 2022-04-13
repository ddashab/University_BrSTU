class Otdel_kadrov:
    count = 0 
    name = str()
    age = int()
    salary = int()

    def __init__(self):
        Otdel_kadrov.count += 1
        print ("Количество: ", Otdel_kadrov.count)

    def __init__(self, name = "", age = 0, salary = 0):
        Otdel_kadrov.count += 1
        print ("Количество: ", Otdel_kadrov.count)
        try:
            self.name = name
            self.age = age
            self.salary = salary
        except ValueError as error:
            print (error)

    def set_name(self, name):
        self.name = name
    def set_age(self, age):
        self.age = age
    def set_salary(self, salary):
        self.salary = salary

    def get_name(self):
        return self.name
    def get_age(self):
        return self.age
    def get_salary(self):
        return self.salary

    def reading(self):
        try:
            self.name = input("Введите имя: ")
            self.age = int(input("Введите возраст: "))
            self.salary = int(input("Введите зарплату ( в USD ): "))
        except ValueError:
            print ("Ошибка ввода")

    def show(self):
        print("\nИмя: ", self.name, "\nВозраст", self.age, "\nЗарплата: ", self.salary, "\n")

member1 = Otdel_kadrov()
member1.set_name("Иванов Иван")
member1.set_age(35)
member1.set_salary(600)
member1.show()

member2 = Otdel_kadrov("Петров Пётр", 27, 550)
member2.show()

member3 = Otdel_kadrov()
member3.reading()
member3.show()

