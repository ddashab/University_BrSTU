class Worker:
	count = 0



	def __init__(self, nm = '', fl = ''):
		Worker.count += 1
		print("Вызов конструктора №", Worker.count)
		try:
			self._name = nm
			self._floor = fl
		except ValueError as e:  # не совпадение типов данных
			print(e)


	def set_name(self, nm):
		self._name = nm

	def set_floor(self, fl):
		self._floor = fl

	def get_name(self):
		return self._name

	def get_floor(self):
		return self._floor

	def read(self):
		try:
			self._name = str(input("Введите имя:  \n"))
			self._floor = str(input("Введите пол:  \n"))
		except ValueError as e:
			print("input error")

	def show(self):
		print("Имя: " + self._name + " Пол: " + self._floor)

	def __del__(self):
		print("Вызов деструткора №", Worker.count)
		Worker.count -= 1

class Musician(Worker):
	_work_experience = int() #трудовой стаж


	def __init__(self, nm='', fl='', we=0):
		Musician.count += 1
		print("Вызов конструктора №", Musician.count)
		try:
			self._name = nm
			self._floor = fl
			self._work_experience = int(we)
		except ValueError as e:  # не совпадение типов данных
			print(e)


	def set_work_experience(self, we):
		self._work_experience = int(we)

	def get_work_experience(self):
		return self._work_experience


	def read(self):
		try:
			self._name = str(input("Введите имя:  \n"))
			self._floor = str(input("Введите пол:  \n"))
			self._work_experience = int(input("Введите трудовой стаж:  \n"))
		except ValueError as e:
			print("input error")

	def show(self):
		print("Имя: " + self._name + " Пол: " + self._floor + " Трудовой стаж: " + str(self._work_experience))

	def __del__(self):
		print("Вызов деструткора №", Musician.count)
		Musician.count -= 1


class Violinist(Musician):
	_type = str()



	def __init__(self, nm='', fl='', we=0, tp=''):
		Violinist.count += 1
		print("Вызов конструктора №", Violinist.count)
		try:
			self._name = nm
			self._floor = fl
			self._work_experience = int(we)
			self._type = tp
		except ValueError as e:  # не совпадение типов данных
			print(e)

	def set_type(self, tp):
		self._type = tp

	def get_type(self):
		return self._type

	def read(self):
		try:
			self._name = str(input("Введите имя:  \n"))
			self._floor = str(input("Введите пол:  \n"))
			self._work_experience = int(input("Введите трудовой стаж:  \n"))
			self._type = str(input("Введите вид скрипки:  \n"))
		except ValueError as e:
			print("input error")

	def show(self):
		print("Имя: " + self._name + " Пол: " + self._floor + " Трудовой стаж: " + str(self._work_experience) +  " Вид скрипки: " + self._type)

	def __del__(self):
		print("Вызов деструктора №", Violinist.count)
		Violinist.count -= 1



if __name__ == '__main__':
	B0 = Violinist()
	B0.read()
	B0.show()

	B1 = Violinist("Диана", "ж", 4, "народная")
	B1.show()

	B2 = Violinist()
	B2.set_name("Марина")
	B2.set_floor("ж")
	B2.set_work_experience(6)
	B2.set_type("классическая")
	B2.show()

