class Bank:
	__counter = 0
	__name = str()
	__monetaryCapital = float()
	__numberOfEmployees = int()

	def __init__(self):
		Bank.__counter += 1
		print(Bank.__counter)

	def __init__(self, nm = "", mc = 0.0, nof = 0):
		Bank.__counter += 1
		print(Bank.__counter)
		self.__name = nm
		self.__monetaryCapital = float(mc)
		self.__numberOfEmployees = int(nof)
			
	def set_name(self, nm):
		self.__name = nm

	def set_capital(self, mc):
		self.__monetaryCapital = float(mc)

	def set_number(self, nof):
		self.__numberOfEmployees = int(nof)

	def get_name(self):
		return self.__name

	def get_capital(self):
		return self.__monetaryCapital

	def get_number(self):
		return self.__numberOfEmployees

	def read(self):
		self.__name = str(input("Enter name: "))
		self.__monetaryCapital = float(input("Enter monetary capital: "))
		self.__numberOfEmployees = int(input("Enter number of employees: "))

	def show(self):
		print("Name: " + self.__name)
		print("Monetary Capital: " + str(self.__monetaryCapital))
		print("Number of employees: " + str(self.__numberOfEmployees))

if __name__ == "__main__":
	y = Bank()
	y1 = Bank()
	y.read()
	y1.read()
	y.show()
	y1.show()



class Sportsman:
	__counter = 0
	__name = str()
	__sport_type = str()
	__age = int()

	def __init__(self):
		Sportsman.__counter += 1
		print(Sportsman.__counter)

	def __init__(self, nm = "", st = "", age = 0):
		Sportsman.__counter += 1
		print("Вызов конструктора №" + str(Sportsman.__counter))
		self.__name = nm  
		self.__sport_type = st
		self.__age = int(age)  

	def __del__(self):
		print("Вызов деструктора №" + str(Sportsman.__counter))
		Sportsman.__counter -= 1

	def set_name(self, nm):
		self.__name = nm  

	def set_st(self, st):
		self.__sport_type = st

	def set_age(self, age):
		self.__age = age  

	def get_name(self):
		return self.__name

	def get_st(self):
		return self.__sport_type

	def get_age(self):
		return self.__age

	def  read(self):
		self.__name = input("Enter name: ")
		self.__sport_type = input("Enter sport type: ")
		self.__age = int(input("Enter age: "))

	def show(self):
		print("Name: " + self.__name)
		print("Sport type: " + self.__sport_type)
		print("Age: " + str(self.__age))

class Person(Sportsman):
	__counter = 0
	__height = float()
	__weight = float()

	def __init__(self):
		pass

	def __init__(self, nm = "", st = "", age = 0, ht = 0.0, wt = 0.0):
		super(Person, self).__init__(nm, st, age)
		self.__height = ht
		self.__weight = wt

	def set_ht(self, ht):
		self.__height = ht  

	def set_wt(self, wt):
		self.__weight = wt

	def get_ht(self):
		return self.__height

	def get_wt(self):  
		return self.__weight

	def read(self):
		self.__name = input("Enter name: ")
		self.__sport_type = input("Enter sport type: ")
		self.__age = int(input("Enter age: "))
		self.__height = float(input("Enter height: "))
		self.__weight = float(input("Enter weight: "))

	def show(self):
		print("Name: " + str(self.__name))
		print("Sport type: " + self.__sport_type)
		print("Age: " + str(self.__age))
		print("Height: " + str(self.__height))
		print("weight: " + str(self.__weight))

class Prize_Winner(Person):
	__counter = 0
	__world_champion = bool()
	__world_ranking = int()

	def __init__(self):
		pass

	def __init__(self, nm = "", st = "", age = 0, ht = 0.0, wt = 0.0, wc = True, wr = 0):
		super(Prize_Winner, self).__init__(nm, st, age, ht, wt)
		self.__world_champion = wc
		self.__world_ranking = wr

	def set_wc(self, wc):
		self.__world_champion = wc  

	def set_wr(self, wr):
		self.__world_ranking = wr

	def get_wc(self):
		return self.__world_champion

	def get_wr(self):  
		return self.__world_ranking

	def read(self):
		self.__name = input("Enter name: ")
		self.__sport_type = input("Enter sport type: ")
		self.__age = int(input("Enter age: "))
		self.__height = float(input("Enter height: "))
		self.__weight = float(input("Enter weight: "))
		check = str(input('Enter is there any world champion: '))
		if check.startswith('True'.lower()):
			self.__world_champion = True
		elif check.startswith('False'.lower()):
			self.__world_champion = False
		self.__world_ranking = int(input("Enter world ranking: "))

	def show(self):
		print("Name: " + self.__name)
		print("Sport type: " + self.__sport_type)
		print("Age: " + str(self.__age))
		print("Height: " + str(self.__height) + " сантиметров")
		print("weight: " + str(self.__weight) + " килограмм")
		print("World champion: " + str(self.__world_champion))
		print("World ranking: " + str(self.__world_ranking))

if __name__ == "__main__":
	P0 = Sportsman()
	P1 = Person() 	
	P2 = Prize_Winner()
	P0.read()
	P1.read()
	P2.read()
	P0.show()
	P1.show()
	P2.show()
