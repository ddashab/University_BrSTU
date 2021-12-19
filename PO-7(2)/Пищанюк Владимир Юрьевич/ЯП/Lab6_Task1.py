import csv
print("Task_1")


class Member_of_Part:
	
	count = 0
	name = str()
	party = str()
	ticket_number = int()

	def __init__(self):
		Member_of_Part.count+=1
		print("Number:",Member_of_Part.count)
	def __init__(self,name="",party="",ticket_number=0):
	    Member_of_Part.count +=1
	    print("Number:",Member_of_Part.count)
	    try:
	        self.name=name
	        self.party=party
	        self.ticket_number=ticket_number
	    except ValueError as error:
	        print(error)

	def set_name(self, name):
		self.name = name
	def set_party(self, party):
		self.party = party
	def set_ticket_number(self, ticket_number):
		self.ticket_number = ticket_number

	def get_name(self):
		return self.name
	def get_party(self):
		return self.party
	def get_ticket_number(self):
		return self.ticket_number

	def reading(self):
		try:
			self.name = input("Enter the name: ")
			self.party = input("Enter the number of people")
			self.ticket_number = int(input("Enter ticket number"))
		except ValueError:
			print ("Error")
	def show(self):
		print("\nName: ", self.name, "\nThe consignment: ", self.party, "\nTicket number: ", self.ticket_number, "\n")

	def write(self,line):
		f=open("D:\\python\\lab6.txt","w",newline="",encoding='utf-8')
		line+=("Name: " + self.name, "The consignment: " + self.party,"Ticket number: " + str(self.ticket_number), " ")
		write=csv.writer(f)
		for i in line:
			line =[''.join(i)]
			write.writerow(line)
		

		f.close()
line=[]
member1 = Member_of_Part()
member1.set_name("Ермаков Нестор Григорьевич")
member1.set_party("AAA")
member1.set_ticket_number(78)
member1.show()
member1.write(line)

member2 = Member_of_Part("Шаров Никита Алексеевич", "BBB", 80)
member2.show()
member2.write(line)

member3 = Member_of_Part()
member3.reading()
member3.show()
member3.write(line)
       	