#include "class1.h"
#include <iomanip>
#define _CRT_SECURE_NO_WARNINGS
//функция для вызова конструктора копирования при построении
//временного объекта как возвращаемого значения функции
Person function(Person& cpPerson) {
	Person temp(cpPerson);
	char* name = new char[50];
	char* streeet = new char[60];
	cin.getline(name, 50);
	cin.getline(streeet, 60);
	temp.set_name(name);
	temp.set_name(streeet);
	return temp;
	delete[]name;
	delete[]streeet;
}
int main() {

	setlocale(0, "");
	system("color f0");
	char* name = new char[50];
	char* streeet = new char[50];
	int number;
	//использование статической памяти

	Person arr1[2];
	cout << setfill('_') << setw(50) << "_" << endl;
	cout << "Enter the name: ";
	cin.getline(name, 50);
	cout << "Enter the street: ";
	cin.getline(streeet, 60);
	cout << "Enter the number of house : ";
	cin >> number;
	cout << endl;
	cout << "Person 1" << endl;
	arr1[0].set(name, streeet, number);
	arr1[0].show();
	//-------------------------
	cin.ignore();
	cout << setfill('_') << setw(50) << "_" << endl;
	cout << "Enter the name: ";
	cin.getline(name, 50);
	cout << "Enter the street: ";
	cin >> streeet;
	cout << "Enter the number of house: ";
	cin >> number;
	cout << endl;
	cout << endl;
	cout << "Person 2" << endl;
	arr1[1].set(name, streeet, number);

	//через указатель доступ

	Person* p = &arr1[1]; //указатель на экземпляр класса
	p->show();
	cin.ignore();
	cout << setfill('_') << setw(50) << "_" << endl;
	//-----------------------
	//использование динамической памяти

	Person* arr2 = new Person[2];
	cout << "Enter the name: ";
	cin.getline(name, 50);
	cin.getline(streeet, 60);
	arr2[0].set(name, streeet, 12);
	arr2[0].show();
	cout << setfill('_') << setw(50) << "_" << endl;
	cout << "Enter the name: ";
	cin.getline(name, 50);
	(&arr1[0])->set(name, streeet, 15);
	(&arr1[1])->view(arr1[1]); //вызов конструктора копирования при передаче функции по значению
	delete[] arr2;
	cout << setfill('_') << setw(50) << "_" << endl;
	cout << "Enter the name: ";
	cin.getline(name, 50);
	cin.getline(streeet, 60);
	Person* object1 = new Person(name, streeet, 17);
	cout << setfill('_') << setw(50) << "_" << endl;

	void(Person:: * pfunction)();
	pfunction = &Person::show; //указатель на компоненту-функцию
	(object1->*pfunction)(); //вывод объекта //по указателю из объекта
	cout << setfill('_') << setw(50) << "_" << endl;

	//вызов конструктора копирования при использовании объекта для инициализации другого объекта

	Person object2 = Person(*object1);
	object2.set_number(12);
	object2.show();
	cout << setfill('_') << setw(50) << "_" << endl;

	//вызов конструктора копирования при построении временного объекта как возвращаемого значения функции

	Person object3 = function(object2);
	object3.show();
	cout << setfill('_') << setw(50) << "_" << endl;
	delete[] name;
	delete object1;
	system("pause");
	return 0;

}
