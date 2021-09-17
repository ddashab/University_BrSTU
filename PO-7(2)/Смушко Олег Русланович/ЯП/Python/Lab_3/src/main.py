from typing import Optional


class Company:
    __counter = 0
    __name: str
    __square: float
    __worker_amount: int

    def __new__(cls, *args, **kwargs):
        Company.__counter += 1
        print(f'Create {cls.__name__}')
        return super().__new__(cls)

    def __init__(self, name: Optional[str] = None, square: Optional[float] = 4500.90, amount: Optional[int] = 50001):
        self.__name = name
        self.__square = square
        self.__worker_amount = amount

    def __del__(self):
        print(f'Del {self.__class__.__name__}')
        Company.__counter -= 1

    def set_name(self, name_) -> None:
        self.__name = name_

    def set_square(self, square_) -> None:
        self.__square = square_

    def set_amount(self, amount_) -> None:
        self.__worker_amount = amount_

    def get_name(self) -> Optional[str]:
        return self.__name

    def get_square(self) -> Optional[float]:
        return self.__square

    def get_amount(self) -> Optional[int]:
        return self.__worker_amount

    def show(self):
        print(f'Name: {self.__name} | Square: {self.__square} m2 | Amount of workers: {self.__worker_amount} '
              f'| Counter: {self.__counter}.')


class Animal:
    counter = 0
    __gender: str
    __color: str
    __age: int

    def __new__(cls, *args, **kwargs):
        Animal.counter += 1
        print(f'Create {cls.__name__}')
        return super().__new__(cls)

    def __init__(self, gender: Optional[str] = '', color: Optional[str] = '', age: Optional[int] = 0):
        self.__gender = gender
        self.__color = color
        self.__age = age

    def __del__(self):
        print(f'Del {self.__class__.__name__}')
        Animal.counter -= 1

    def set_gender(self, gender: str) -> None:
        self.__gender = gender

    def set_color(self, color: str) -> None:
        self.__color = color

    def set_age(self, age: int):
        self.__age = age

    def get_gender(self) -> Optional[str]:
        return self.__gender

    def get_color(self) -> Optional[str]:
        return self.__color

    def get_age(self) -> Optional[int]:
        return self.__age

    def show(self) -> None:
        print(f'Gender: {self.__gender} | Color: {self.__color} | Age: {self.__age} years'
              f' | Counter: {self.counter}.')

    def input(self):
        self.__gender = str(input('Enter gender of the animal: '))
        self.__color = str(input('Enter color: '))
        self.__age = int(input('Enter age: '))


class DomesticAnimal(Animal):
    __is_milk: bool
    __weight: float

    def __init__(self, gender: Optional[str] = '', color: Optional[str] = '', age: Optional[int] = 0,
                 weight: Optional[float] = 0, is_milk: Optional[bool] = False):
        super().__init__(gender, color, age)
        self.__is_milk = is_milk
        self.__weight = weight

    def set_is_milk(self, is_milk: bool) -> None:
        self.__is_milk = is_milk

    def set_weight(self, weight: float):
        self.__weight = weight

    def get_is_milk(self) -> Optional[bool]:
        return self.__is_milk

    def get_weight(self) -> Optional[float]:
        return self.__weight

    def show(self) -> None:
        print(f'Gender: {self.get_gender()} | Color: {self.get_color()} | Age: {self.get_age()} years'
              f' | Counter: {self.counter} | Milk? {self.__is_milk} | Weight: {self.__weight}.')

    def input(self):
        self.set_gender(str(input('Enter gender of the animal: ')))
        self.set_color(str(input('Enter color: ')))
        self.set_age(int(input('Enter age: ')))
        check = str(input('Enter is there any milk: '))
        if check.startswith('True'.lower()):
            self.__is_milk = True
        elif check.startswith('False'.lower()):
            self.__is_milk = False
        self.__weight = float(input('Enter weight: '))


class Dog(DomesticAnimal):
    __speed: float
    __breed: str

    def __init__(self, gender: Optional[str] = '', color: Optional[str] = '', age: Optional[int] = 0,
                 weight: Optional[float] = 0, speed: Optional[float] = 0,
                 breed: Optional[str] = '', is_milk: Optional[bool] = False):
        super().__init__(gender, color, age, weight, is_milk)
        self.__speed = speed
        self.__breed = breed

    def set_speed(self, speed: float) -> None:
        self.__speed = speed

    def set_breed(self, breed: str):
        self.__breed = breed

    def get_speed(self) -> Optional[float]:
        return self.__speed

    def get_breed(self) -> Optional[str]:
        return self.__breed

    def show(self):
        print(f'Gender: {self.get_gender()} | Color: {self.get_color()} | Age: {self.get_age()} years'
              f' | Counter: {self.counter} | Milk? {self.get_is_milk()} | Weight: {self.get_weight()}'
              f' | Speed: {self.__speed} km/h | Breed: {self.__breed}.')

    def input(self):
        self.set_gender(str(input('Enter gender of the animal: ')))
        self.set_color(str(input('Enter color: ')))
        self.set_age(int(input('Enter age: ')))
        check = str(input('Enter is there any milk: '))
        if check.startswith('True'.lower()):
            self.set_is_milk(True)
        elif check.startswith('False'.lower()):
            self.set_is_milk(False)
        self.set_weight(float(input('Enter weight: ')))
        self.__speed = float(input('Enter speed: '))
        self.__breed = str(input('Enter breed: '))


def main():
    def task_1():
        print('Task 1')
        name = str(input('Enter company\'s name: '))
        square = float(input('Enter square of the company: '))
        amount = int(input('Enter amount of workers: '))

        cmp1 = Company()
        cmp1.set_name(name)
        cmp1.set_square(square)
        cmp1.set_amount(amount)
        cmp1.show()

        cmp2 = Company("Apple", 1725.56, 110500)
        cmp2.show()
        cmp2.__del__()

        cmp3 = Company()
        cmp3.set_name("Xiaomi")
        cmp3.show()

    def task_2():

        def check(val: str) -> bool:
            if val.startswith('True'.lower()):
                val = True
                return val
            elif val.startswith('False'.lower()):
                val = False
                return val
        print('\nTask 2')
        gender = str(input('Enter gender of the animal: '))
        color = str(input('Enter color: '))
        age = int(input('Enter age: '))

        anm1_1 = Animal(gender, color, age)
        anm1_1.show()
        anm1_2 = Animal("Male", "Green", 8)
        anm1_2.show()

        is_milk = check(str(input('Enter is there any milk: ')))
        weight = float(input('Enter weight of the animal: '))
        anm2_1 = DomesticAnimal(gender, color, age, weight, is_milk)
        anm2_1.show()
        anm2_2 = DomesticAnimal("Female", "Red", 11, 89.60, False)
        anm2_2.show()

        speed = float(input('Enter speed: '))
        breed = str(input('Enter breed: '))
        anm3_1 = Dog(gender, color, age, weight, speed, breed, is_milk)
        anm3_1.show()
        anm3_2 = Dog("Male", "Brown", 2, 14.50, 55, "Labrador")
        anm3_2.show()
        anm3_2.set_color('White')
        print(f'Color: {anm3_2.get_color()}.')

        animal_3 = Dog()
        animal_3.input()
        animal_3.show()

    task_1()
    task_2()


if __name__ == '__main__':
    main()
