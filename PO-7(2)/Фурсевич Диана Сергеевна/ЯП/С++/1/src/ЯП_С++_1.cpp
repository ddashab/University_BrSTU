#include "class.h"

Person fun() {
	//cout << "Вызвалась функция fun" << endl;
	char*name = new char[100];
	cin.getline(name, 100);
	Person p(name, 45, 0);
	//cout << "Конец функции fun" << endl;
	return p;

}


int main()
{
	setlocale(LC_ALL, "ru");


	char* name = new char[100];
	Person array[1];//использование статической памяти 
	cin.getline(name, 100);
	array[0].SET(name, 12, 1);
	array[0].Show();
	cout << endl;



	Person *point = &array[0]; //указатель на объект класса
	point->Show();// вывод данных через указатель

	/*
	point->SETFloor(0);
	cout << "указатель: " << endl;
	point->Show();
	cout << "объект класса: " << endl;
	array[0].Show();*/

	Person *array_1 = new Person[2]; //использование динамической памяти

	cin.getline(name, 100);
	array_1->SET(name, 34, 2);
	array_1[0].Show();
	cout << endl;

	cin.getline(name, 100);
	(array_1 + 1)->SET(name, 65, 2);
	(array_1 + 1)->View(array_1[1]); //вызов конструктора копирования, когда объект передаётся функции по значению
	cout << endl;
	delete[] array_1;


	//использование указателя на компонентную функцию
	void(Person::*pf)();//определение указателя на компоненту-функцию
	pf = &Person::Show; //настройка указателя 
	cin.getline(name, 100);
	Person *example = new Person(name, 23, 2);
	(example->*pf)(); //вывод объекта

	Person example_2 = Person(*example);//вызов конструктора копирования при использовании объекта для инициализации другого объекта
	example_2.Show();


	Person example_3 = fun();//вызов конструктора копирования при построении временного объекта как возвращаемого значения функции

	delete example;
	delete[] name;

}


