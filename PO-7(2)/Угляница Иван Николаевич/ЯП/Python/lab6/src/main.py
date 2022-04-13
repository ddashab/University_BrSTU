class Apartment:
    count = 0

    def __init__(self, n_square=20, n_price=300, n_city="Brest"):
        Apartment.count += 1
        self.__square = n_square
        self.__price = n_price
        self.__city = n_city
        print(f"Constructor worked {Apartment.count} time")

    @property
    def square(self) -> int:
        return self.__square

    @square.setter
    def square(self, n_square) -> None:
        self.__square = n_square

    @property
    def price(self) -> int:
        return self.__price

    @price.setter
    def price(self, n_price) -> None:
        self.__price = n_price

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, n_city) -> None:
        self.__city = n_city

    def Show(self) -> None:
        print(f"Square = {self.__square},Price = {self.__price},City = {self.__city}")


def main():
    flat1 = Apartment()
    flat2 = Apartment(21, 450, "Minsk")
    flat1.Show()
    flat2.Show()
    flat1.square = 777
    print(flat1.square)
    flat1.Show()


if __name__ == "__main__":
    main()
