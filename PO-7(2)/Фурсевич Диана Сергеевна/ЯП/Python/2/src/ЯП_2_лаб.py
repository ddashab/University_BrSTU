import csv
import os

FILENAME = "students.csv"


def f_1():
	# print("Текущая директория: ", os.getcwd())
	# print("Все папки и файлы: ", os.listdir())

	path = os.getcwd()
	count = 0

	for root, dirs, files in os.walk(path):
		# путь к каталогу
		print(root)
		for _dir in dirs:  # список каталогов
			print(_dir)

		for _file in files:  # список файлов
			print(_file)
			count += 1
		break
	print("Количество файлов в данной директории {} : {}".format(path, count))


# запись первоначальных данных в файл
def write_file_new(File_Name):
	list = [['№','ФИО','Возраст','Группа'],['1','Иванов Иван Иванович','23','БО-11'],['2','Сидоров Семен Семенович','23','БО-23'],
	['3','Яшков Илья Петрович','24','БО-123']]
	with open(File_Name, 'w', newline="") as file:
		writer = csv.writer(file)
		for i in list:
			line = [';'.join(i)]
			writer.writerow(line)


# вывод данных
def output_data_2(list):
	for i in list:
		for j in range(len(i)):
			print(i[j], end=' ')
		print()


# чтение данных из файла
def read_file(File_Name):
	list = []
	with open(File_Name, 'r', newline="") as file:
		reader = csv.reader(file)
		for i in reader:
			list.append(str(i)[2:len(i) - 3].split(';'))
	print(list)
	return list


# запись данных в файл
def write_file(File_Name, new_l):
	with open(File_Name, 'w', newline="") as file:
		cap = ["№;ФИО;Возраст;Группа"]
		writer = csv.writer(file)
		writer.writerow(cap)
		for row in new_l:
			line = [';'.join(row)]
			writer.writerow(line)
	file.close()


def key_sort(l):
	return int(l[3][3:])

# сортировка данных по номеру группы
def f_2():

	list = read_file(FILENAME)
	print("Исходная информация: ", list)
	output_data_2(list)
	new_l = []
	for i in list[1:]:
		new_l.append(i)
	new_l.sort(key=key_sort)
	print("Отсортированный список по номеру группы: ", new_l, "\n")
	print("Записать данные в файл: 0-нет, 1-да")
	n = int(input())
	if n != 0:
		write_file(FILENAME, new_l)



# уменьшение в данной группе возрастов на 1
def f_3():

	list = read_file(FILENAME)
	new_l = []
	for i in list[1:]:
		new_l.append(i)
	print(new_l)
	number = input("\nВведите номер группы: ")
	for i in range(len(new_l)):
		if new_l[i][3] == number:
			new_l[i][2] = str(int(new_l[i][2]) - 1)
	print(new_l)
	print("Записать данные в файл: 0-нет, 1-да")
	n = int(input())
	if n != 0:
		write_file(FILENAME, new_l)




if __name__ == '__main__':
	write_file_new(FILENAME)
	while True:
		print("Введите номер задани (0 - выход)")
		number = int(input())
		if number == 0:
			break
		elif number == 1:
			f_1()
		elif number == 2:
			f_2()
		elif number == 3:
			f_3()
		elif number == 4:
			read_file(FILENAME)
0


