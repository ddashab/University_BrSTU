class Graduate:
    counter = 0

    def __init__(self, name="Igor", faculty="FEIS", year_release=2024):
        Graduate.counter += 1
        print(f"Now we have {Graduate.counter} people")
        self.__name = name
        self.__faculty = faculty
        self.__year_release = year_release
        print(f'{self.counter} constructor')

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name) -> None:
        self.__name = name

    @property
    def faculty(self) -> str:
        return self.__faculty

    @faculty.setter
    def faculty(self, faculty) -> None:
        self.__faculty = faculty

    @property
    def year(self) -> int:
        return self.__year_release

    @year.setter
    def year(self, year) -> None:
        if year.isdigit():
            self.__year_release = year
        else:
            print("Wrong number")

    def show(self) -> None:
        print(f"Name - {self.__name}, Faculty name - {self.__faculty}, Release year - {self.__year_release}")

    def read(self) -> None:
        self.__name = input("Input Name - ")
        self.__faculty = input("Input your faculty name - ")
        try:
            self.__year_release = int(input("Input your release year -"))
        except ValueError:
            print("Bro, u need write number, not string.")


class Person:
    def __init__(self, name: str = "Igor", age: int = 18, sex: str = "Man"):
        self._name = name
        self._age = age
        self._sex = sex
        print(f"Person constructor for {type(self).__name__} worked")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, age: str) -> None:
        if age.isdigit():
            self._age = int(age)
        else:
            print("Wrong number")

    @property
    def sex(self) -> str:
        return self._sex

    @sex.setter
    def sex(self, sex: str) -> None:
        self._sex = sex

    def show(self) -> None:
        print(f"Name - {self._name}")
        print(f"Age - {self._age}")
        print(f"Sex - {self._sex}")

    def __del__(self):
        print(f"Destructor for {type(self).__name__} worked")

    def console_set(self):
        self._name = input("Input your name -")
        try:
            self._age = int(input("Input your age -"))
        except ValueError:
            print("Bro, u need write number, not string.")
        self._sex = input("Input your sex -")


class Student(Person):
    def __init__(self, name: str = "Igor", age: int = 18, sex: str = "Man", course: int = 2):
        super().__init__(name, age, sex)
        self._course = course
        print(f"Student constructor for {type(self).__name__} worked")

    @property
    def course(self) -> int:
        return self._course

    @course.setter
    def course(self, course: str) -> None:
        if course.isdigit():
            self._course = int(course)
        else:
            print("Wrong number")

    def show(self) -> None:
        super().show()
        print(f"Course number - {self._course}")

    def console_set(self):
        super().console_set()
        try:
            self._course = int(input("Input your course number -"))
        except ValueError:
            print("Bro, u need write number, not string.")


class SportsMan(Student):
    def __init__(self, name: str = "Igor", age: int = 18, sex: str = "Man", course: int = 2, medals_amount: int = 5):
        super().__init__(name, age, sex, course)
        self._medals_amount = medals_amount
        print(f"Sportsman constructor for {type(self).__name__} worked")

    @property
    def medals(self) -> int:
        return self._medals_amount

    @medals.setter
    def medals(self, medals: str) -> None:
        if medals.isdigit():
            self._medals_amount = int(medals)
        else:
            print("Wrong number")

    def show(self) -> None:
        super().show()
        print(f"Medals amount - {self._medals_amount}")

    def console_set(self):
        super().console_set()
        try:
            self._medals_amount = int(input("Input your medals amount -"))
        except ValueError:
            print("Bro, u need write number, not string.")


def main():
    input("Task 1. Press Enter")
    graduate_1 = Graduate()
    graduate_1.show()
    graduate_1.year = input("Input ur release year -")
    graduate_1.show()
    graduate_1.read()
    graduate_1.show()
    graduate_2 = Graduate("Aloha", "FISE")
    graduate_2.show()
    input("Task 2. Press Enter")
    person = Person()
    person.show()
    student = Student("Boris", 25, "Man")
    print(student.age)
    sportsman = SportsMan("Anna", 50, "Woman", 2, 1000)
    sportsman.console_set()


if __name__ == "__main__":
    main()
