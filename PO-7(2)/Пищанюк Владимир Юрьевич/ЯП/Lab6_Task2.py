import csv
class Person:
	
	name = str()
	def __init__(self):
		print("The constructor for the Persona class was called, without parameters: ",self)
	def __init__(self,name=""):
		print("The constructor for the Person class was called, with parameters: ",self)
		try:
			self.name=name
		except ValueError as error:
			print(error)
	def __del__(self):
		print("Destructor for Persona was called:",self)
		
	def set_name(self,name):
	    self.name=name
	def get_name(self):
	    return self.name 

	def print(self):
	    print("Name: ",self.name,"\n")

	def reading(self):
		try:
			self.name=input("Enter the Name: ")
		except ValueError as error:
			print(error)

	def write(self,arr):
		f=open("D:\\temp1_for_lab3_py.txt","w",newline="",encoding="utf-8")
		arr+=("Name: "+self.name," ")
		write = csv.writer(f)
		for i in arr:
			arr=[''.join(i)]
			write.writerow(arr)
		f.close()	

class schoolPer(Person):
	marks =int()
	def __init__(self):
		print("The constructor for the schoolPer class was called, without parameters: ",self)
	def __init__(self,name ="",marks=0):
	    print("The constructor for the schoolPer class was called, with parameters: ",self)
	    try:
	        self.name=name
	        self.marks=marks
	    except ValueError as error:
	        print(error)
	def __del__(self):
	    print("Destructor for schoolPer was called: ",self)

	def set_marks(self,marks):
	    self.marks=marks	
	def get_marks(self):
		return self.marks

	def print(self):
		print("Name: ",self.name)
		print("Point: ",self.marks,"\n")

		def reading(self):
			try:
				self.name=input("Enter the Name: ")
				self.marks=int(input("Enter the points of the Person: "))
			except ValueError as error:
				print(error)

	def write(self,arr):
		f=open("D:\\temp2_for_lab3_py","w",newline="",encoding="utf-8")
		arr+=("Name: "+self.name,"Marks: "+str(self.marks)," ")
		write = csv.writer(f)
		for i in arr:
			arr=[''.join(i)]
			write.writerow(arr)
		f.close()



class Teacher(schoolPer):
	education = str()
	def __init__(self):
		print("The constructor for the Teacher class was called, without parameters: ",self)
	def __init__(self,name="",marks=0,education=""):
		print("The constructor for the Teacher class was called, with parameters: ",self)
		try:
			self.name=name
			self.marks=marks
			self.education=education
		except ValueError as error:
			print(error)
		def __del__(self):
		    print("Destructor for schoolPer was called: ", self)

	def set_education(seld,education):
		self.education=education
	def get_education(self):
		return self.education

	def print(self):
		print("Name: ",self.name)
		print("Mark: ",self.marks)
		print("Education: ",self.education)

	def reading(self):
		try:
			self.name=input("Enter the Name: ")
			self.marks=int(input("Enter the points of person: "))
			self.education=input("Enter the education of persona: ")
		except ValueError as error:
			print(error)

	def write(self,arr):
		f=open("D:\\temp2_for_lab3_py","w",newline="",encoding="utf-8")
		arr+=("Name: "+self.name,"Marks: "+str(self.marks),"Education: "+self.education," ")
		write = csv.writer(f)
		for i in arr:
			arr=[''.join(i)]
			write.writerow(arr)
		f.close()



arr=[]

object1=Person()
object1.set_name("Vova")
object1.print()
object1.write(arr)

object2=schoolPer("Gleb", 12)
object2.print()
object2.write(arr)

object3=Teacher()
object3.reading()
object3.print()
object3.write(arr)


