class Diplomat:
	count = 0
	__nationality = str()
	__age = int()
	__job_assignment_country = str()

	def __init__(self):
		Diplomat.count += 1
		print("Создание объекта №", Diplomat.count)

	def __init__(self, nt='', ag=0, jac=''):
		Diplomat.count += 1
		print("Создание объекта №", Diplomat.count)
		try:
			self.__nationality = nt
			self.__age = int(ag)
			self.__job_assignment_country = jac
		except ValueError as e:  # не совпадение типов данных
			print(e)

	def set_natinality(self, nt):
		self.__nationality = nt

	def set_age(self, ag):
		self.__age = int(ag)

	def set_job_assignment_country(self, jas):
		self.__nationality = jas

	def get_natinality(self):
		return self.__nationality

	def get_age(self):
		return self.__age

	def get_job_assignment_country(self):
		return self.__nationality

	def read(self):
		try:
			self.__nationality = str(input("Введите национальность:  \n"))
			self.__age = int(input("Введите возраст:  \n"))
			self.__job_assignment_country = str(input("Введите назначение страны:  \n"))
		except ValueError as e:
			print("input error")

	def show(self):
		print("Национальность: " + self.__nationality + " Возраст: " + str(self.__age) + " Назначение страны: " + self.__job_assignment_country)

	def __del__(self):
		print("Деструктор №", Diplomat.count)
		Diplomat.count -= 1

if __name__ == '__main__':
	y = Diplomat()
	y1 = Diplomat()
	y.read()
	y1.read()
	y.show()
	y1.show()

	x = Diplomat("россиян", 23, "Польша")
	x.show()
	c = Diplomat()
	c.set_natinality("итальянец")
	c.set_age(34)
	c.set_job_assignment_country("Германия")
	c.show()