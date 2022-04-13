import numpy as np
import pandas as pd
import random

def task1_1():
	a = int(input("Enter the number A: "))
	if a == 0:
		a = int(input("Change count A: "))
	b = int(input("Enter the number B: "))
	if b == 0:
		b = int(input("Change count B:"))
	c = int(input("Enter the number C: "))
	k = int(input("Enter the number K: "))
	sum = (((a**2)/(b**2))+(c**2)*(a**2))/(a+b+c*(k-a/(b**3)))+c+(k/b-k/a)*c
	if sum < 0:
		print(abs(sum))
	else:
		print(sum)

def task1_2():
	list_a = []
	list_b = []
	for i in range(10):
		list_a.append(random.randint(0, 10))
	print(list_a)
	for i in list_a:
		if i % 2 == 0:
			list_b.append(i)
	print(list_b)

def task1_3():
	strcount = [1, 4, 12, 7, 5, 13, 7, 10]
	sum1 = []
	print(strcount)
	for i in strcount:
		if i >= 10:
			sum1.append(i)
	print(sum1)
	print(sum(sum1))

def task1_4():
	strcount = [1, 4, 12, 7, 5, 13, 7, 10]
	print(max(strcount))

def task2_1():
	my_number = 5
	user_number = int(input("Enter the number"))

	if my_number == user_number:
		print("This is 5")
	else:
		print("Try again")
		input(user_number)



def task2_2():
	list_str = ['world', 'Space', 'Documentation', 'Unreal Engine']
	i = 0
	while len(list_str) > i:
		if len(list_str[i]) > 5 :
			if len(list_str[i]) < 10:
				print(list_str[i])
		i += 1

def	task2_4():
	text = [random.choice('abc123') for _ in range(10)]
	text[5] = random.choice('ABC')
	random_string = ''.join(text)
	print(random_string)
	str2 = ''
	for c in random_string:
		if c not in ('abcABC'):
			str2 = str2 + c
	print(str2)

def task3_1():
	matrix = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
					   [8, 7, 6, 5, 4, 3, 2, 1,],
					   [2, 3, 4, 5, 6, 7, 8, 9],
					   [9, 8, 7, 6, 5, 4, 3, 2],
					   [1, 3, 5, 7, 9, 7, 5, 3],
					   [3, 1, 5, 3, 2, 6, 5, 7],
					   [1, 7, 5, 9, 7, 3, 1, 5],
					   [2, 6, 3, 5, 1, 7, 3, 2]])
	print(matrix)
	new_matrix = matrix*matrix
	print(new_matrix)

def task3_2():
	matrix = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
					   [8, 7, 6, 5, 4, 3, 2, 1,],
					   [2, 3, 4, 5, 6, 7, 8, 9],
					   [9, 8, 7, 6, 5, 4, 3, 2],
					   [1, 3, 5, 7, 9, 7, 5, 3],
					   [3, 1, 5, 3, 2, 6, 5, 7],
					   [1, 7, 5, 9, 7, 3, 1, 5],
					   [2, 6, 3, 5, 1, 7, 3, 2]])
	print(matrix)
	for row in matrix:
		print(np.sum(row))

def task3_3():
	matrix = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
					   [8, 7, 6, 5, 4, 3, 2, 1,],
					   [2, 3, 4, 5, 6, 7, 8, 9],
					   [9, 8, 7, 6, 5, 4, 3, 2],
					   [1, 3, 5, 7, 9, 7, 5, 3],
					   [3, 1, 5, 3, 2, 6, 5, 7],
					   [1, 7, 5, 9, 7, 3, 1, 5],
					   [2, 6, 3, 5, 1, 7, 3, 2]])
	print(matrix)
	for row in matrix:
		row_matrix = row
		print(np.prod(np.array(row_matrix)))

def task3_4():
	matrix = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
					   [8, 7, 6, 5, 4, 3, 2, 1,],
					   [2, 3, 4, 5, 6, 7, 8, 9],
					   [9, 8, 7, 6, 5, 4, 3, 2],
					   [1, 3, 5, 7, 9, 7, 5, 3],
					   [3, 1, 5, 3, 2, 6, 5, 7],
					   [1, 7, 5, 9, 7, 3, 1, 5],
					   [2, 6, 3, 5, 1, 7, 3, 2]])
	print(matrix)
	for row in matrix:
		for el in row:
			if el == 5:
				matrix[matrix == el] = el*el
	print(matrix)

def task3_5():
	matrix = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
					   [8, 7, 6, 5, 4, 3, 2, 1,],
					   [2, 3, 4, 5, 6, 7, 8, 9],
					   [9, 8, 7, 6, 5, 4, 3, 2],
					   [1, 3, 5, 7, 9, 7, 5, 3],
					   [3, 1, 5, 3, 2, 6, 5, 7],
					   [1, 7, 5, 9, 7, 3, 1, 5],
					   [2, 6, 3, 5, 1, 7, 3, 2]])
	print(matrix)

def task3_6():
	matrix = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
					   [8, 7, 6, 5, 4, 3, 2, 1,],
					   [2, 3, 4, 5, 6, 7, 8, 9],
					   [9, 8, 7, 6, 5, 4, 3, 2],
					   [1, 3, 5, 7, 9, 7, 5, 3],
					   [3, 1, 5, 3, 2, 6, 5, 7],
					   [1, 7, 5, 9, 7, 3, 1, 5],
					   [2, 6, 3, 5, 1, 7, 3, 2]])
	print(matrix)
	set = []
	for row in matrix:
		for el in row:
			if el == 3:
				set.append(el)
	print(len(set))

def task3_7():
	matrix = np.array([[1, 2, 3, 4, 5, 6, 7, 8],
					   [8, 7, 6, 5, 4, 3, 2, 1,],
					   [2, 3, 4, 5, 6, 7, 8, 9],
					   [9, 8, 7, 6, 5, 4, 3, 2],
					   [1, 3, 5, 7, 9, 7, 5, 3],
					   [3, 1, 5, 3, 2, 6, 5, 7],
					   [1, 7, 5, 9, 7, 3, 1, 5],
					   [2, 6, 3, 5, 1, 7, 3, 2]])
	print(matrix)
	a = int(input('Enter the line number: '))
	b = int(input('Enter the column number: '))
	print(matrix[a,b])

def task4_1():
	str = 'Cold, Summer, Brest, Toyota, Pen, Pencil, Python, C++, C#'
	new_str = str.split()
	for word in new_str:
		if len(word) > 6:
			print(word)

def task4_2():
	my_string = 'Full Name; Age; Category; Praktika; Daniil; Olegovich; 18 Years; student 2rd year university student; Osmush; Artur; Igorevich; 18 years; student 3rd year university student'
	spisok = pd.DataFrame({
		"ФИО                 ": ['Praktika Daniil Olegovich', 'Osmush Artur Igorevich'],
		"Категория": ['student 2rd year university student', 'student 3rd year university student'],
		"Возраст": ['18 Years', '18 years']
	})
	print(spisok)

def task4_3():
	my_len = (
	        "Full Name;Age;Category;"
	        "_Ivan Ivanov Ivanovich;22 Years;student 2rd year university student;"
			"_Petr Molo Ivanovich;22 Years;student 2rd year university student;"
			"_Max Lolo Ivanovich;22 Years;student 3rd year university student;"
			"_Igor Solo Ivanovich;22 Years;student 2rd year university student;"
			"_Daniil Void Ivanovich;22 Years;student 3rd year university student;"
			"_Denis Salat Ivanovich;22 Years;student 2rd year university student;"
	   )
	students = my_len.split(";_")
	data_new = []
	info = []
	for row in students:
		data_new.append(row.split(";"))
	for i in data_new:
		if "Lolo" in i[0]:
			info.append(i)
	for i in info:
			print(" ".join(i))

def task4_4():
	s = 'Короче, Меченый, я тебя спас и в благородство играть не буду: ' \
		'выполнишь для меня пару заданий — и мы в расчете.' \
		' Заодно посмотрим, как быстро у тебя башка после амнезии прояснится. ' \
		'А по твоей теме постараюсь разузнать. Хрен его знает, на кой ляд тебе этот Стрелок сдался, ' \
		'но я в чужие дела не лезу, хочешь убить, значит есть за что...'
	print(len(s.split()))
	print(len(s))

def task6_1():
	matrix1 = np.random.randint(10, size=(4, 4))
	print(matrix1)
	print(np.sum(matrix1))

def task6_2():
	my_set = []
	my_set1 = []
	for i in range(10):
		my_set.append(random.randint(0,100))
	print(my_set)
	del my_set[0]
	del my_set[0]
	print(my_set)
	my_set.append(555555555555)
	my_set.append(0)
	print(my_set)

def task6_3():
	group = [["БО-331101", ["Акулова Алена", "Бабушкина Ксения"]], ["БО-402000", ["Альфа Миша", "Альфа Рома"]]]
	number = 'БО-331101'
	result = pd.Series(['БО-331101:      ', 'Акулова Алена   ', 'Бабушкина Ксения'])
	print(result)

def menu():
	print("1 - Task 1.1")
	print("2 - Task 1.2")
	print("3 - Task 1.3")
	print("4 - Task 1.4")
	print("0 - Exit")
	a = int(input("Enter number: "))
	if a==1:
		task1_1()
	if a==2:
		task1_2()
	if a==3:
		task1_3()
	if a == 4:
		task1_4()
	if a == 0:
		print("Exit")
		exit()
	print("Do you want to continue?")
	b = input("Yes/No\n")
	if b == "Yes":
		menu()
	if b == "No":
		exit()

menu()
