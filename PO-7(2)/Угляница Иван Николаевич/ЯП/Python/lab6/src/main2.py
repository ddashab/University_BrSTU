class Learner:
    def __init__(self, n_name="Ivan", n_birth="06.07.2003"):
        self._name = n_name
        self._birth = n_birth
        print("Constructor worked for Learner")

    def __del__(self):
        print(f"destructor worked{self._name}")

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, n_name) -> None:
        self._name = n_name

    @property
    def birth(self) -> str:
        return self._birth

    @birth.setter
    def birth(self, n_birth) -> None:
        self._birth = n_birth


class Student(Learner):
    def __init__(self, n_name="Ivan", n_birth="06.07.2003", n_faculty="FEIS"):
        super().__init__(n_name, n_birth)
        self.__faculty = n_faculty
        print("Constructor worked for Student")

    def __del__(self):
        print(f"Destructor worked for class student")

    def show(self) -> None:
        print(f"Student: {self._name} {self._birth} faculty: {self.__faculty}")

    def input_data(self) -> None:
        self._name = input("Input student name ")
        self._birth = input("Input student birthday ")
        self.__faculty = input("Input student faculty ")

    @property
    def faculty(self) -> str:
        return self.__faculty

    @faculty.setter
    def faculty(self, n_faculty) -> None:
        self.__faculty = n_faculty


class Undergraduate(Learner):
    def __init__(self, n_name="Ivan", n_birth="06.07.2003", n_direction=""):
        super(Undergraduate, self).__init__(n_name, n_birth)
        self.__direction = n_direction
        print("Constructor worked for undergraduate")

    def __del__(self):
        print("Destructor worked for undergraduate")

    def show(self) -> None:
        print(
            f"Undergraduate: {self._name} {self._birth} direction: {self.__direction}"
        )

    def input_data(self) -> None:
        self._name = input("Input student name ")
        self._birth = input("Input student birthday ")
        self.__direction = input("Input student direction ")

    @property
    def direction(self) -> str:
        return self.__direction

    @direction.setter
    def direction(self, n_direction) -> None:
        self.__direction = n_direction


def main():
    s1 = Student()
    s1.input_data()
    s1.show()
    u1 = Undergraduate()
    u1.birth = "777"
    u1.show()

if __name__ == "__main__":
    main()
