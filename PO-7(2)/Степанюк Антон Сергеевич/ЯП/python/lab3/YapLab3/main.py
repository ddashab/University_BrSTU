
class Company:
    count = 0
    __name = str()
    __num_employee = int()
    __product_type = str()

    def __init__(self):
        Company.count += 1
        print(Company.count)
        print('1 st AAAAAAAAAAAAAAAAAAAAAAa')

    def __init__(self, name='', num_employee=0, product_type=''):
        Company.count += 1
        print(Company.count)
        print('2 st BBBBBBBBBBBBBBBBBBBBBBBBBBB')

        try:
            self.__name = name
            self.__num_employee = num_employee
            self.__product_type = product_type
        except ValueError as e:
            print(e)

    def set_name(self, name):
        self.__name = name

    def set_num_employee(self, num_employee):
        self.__num_employee = num_employee

    def set_product_type(self, product_type):
        self.__product_type = product_type

    def get_name(self):
        return self.__name

    def get_num_employee(self):
        return self.__num_employee

    def get_product_type(self):
        return self.__product_type

    def read(self):
        try:
            self.__name = str(input("Введите название предприятия: "))
            self.__num_employee = int(input("Введите количество работников: "))
            self.__product_type = str(input("Введите тип производимого продукта: "))
        except ValueError as e:
            print(e)

    def show(self):
        print("Название компании: " + self.__name + " Количество работников: " + str(self.__num_employee) + " Тип производимого продукта: " + self.__product_type)


def main():
    valve = Company()
    microsoft = Company()
    valve.read()
    microsoft.read()
    valve.show()
    microsoft.show()
    microsoft = Company('Виндовс', 33, 'виндовс')
    microsoft.set_name('Майкрософт')
    microsoft.show()


if __name__ == '__main__':
    main()