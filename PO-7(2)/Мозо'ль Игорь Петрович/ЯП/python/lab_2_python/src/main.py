import os
import csv
from pprint import pprint

def read_data_from_file(filename): #считываем информацию из файла и разбиваем по \n
    if os.path.exists(filename)==False:
        return None
    with open(filename, "r", encoding='utf-8') as file:
        return file.read().split('\n')

def transform_csv_to_arr(arr,filename): #преобразовываем информацию из прошлой функции
    for i in read_data_from_file(filename)[1:]:
        arr.append(i.split(';'))

def sorted_by_Surname(arr): #сортируем информацию по фамилии
    arr.sort(key=lambda student: student[1])

def write_in_file(arr,filename):
    with open(filename, "w") as file:
        file.write('№;ФИО;Возраст;Группа\n')
        count=1
        for i in arr:
            file.write(";".join(i))
            if count!=len(arr):
                file.write('\n')
            count+=1

def task_1():
    print("There is {} files in directory".format(len(os.listdir('test_dir'))))

def reduce_age_by_one(arr):
    for i in arr:
        i[2]=str(int(i[2])-1)

def main():
    arr=[]
    choose=1
    while 1<=choose<=6:
        print("What do u want to do?\n1.Print the amount of files in directory('test_dir')")
        print("2.Read and print information from file\n3.Reduce the age of students by 1\n4.Sort students by surname")
        print("5.Print list\n6.Write info into file")
        choose=int(input("Your choose - "))
        if choose==1:
            task_1()
        elif choose==2:
            arr=[]
            filename=input("Input name of file - ")
            if read_data_from_file(filename)!=None:
                transform_csv_to_arr(arr,filename)
                pprint(arr)
            else:
                print("Can't read from this file, sry")
        elif choose==3:
            reduce_age_by_one(arr)
        elif choose==4:
            sorted_by_Surname(arr)
        elif choose==5:
            pprint(arr)
        elif choose==6:
            filename=input("Input name of file - ")
            write_in_file(arr,filename)
        else:
            print("ББ мужик")

main()