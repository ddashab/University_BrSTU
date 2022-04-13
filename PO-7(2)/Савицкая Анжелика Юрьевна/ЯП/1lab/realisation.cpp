#include "class1.h"

Person::Person(char* name, char* streeet, int number) {
	Person_name = name;
	Street = streeet;
	House = number;
	cout << " Конструктор с параметрами " << this << endl;
}

Person::Person() {
	cout << " Конструктор без параметров " << this << endl;

}

Person::Person(const Person& copyPerson) {
	Person_name = copyPerson.Person_name;
	House = copyPerson.House;
	Street = copyPerson.Street;
	cout << " Конструктор копирования " << this << endl;

}

Person::~Person() {
	cout << " Деструктор " << this << endl;

}

void Person::set_name(char* name) {
	Person_name = name;

}

void Person::set_streeet(char* streeet) {
	Street = streeet;
}
void Person::set_number(int number) {
	House = number;
}

void Person::set(char* name, char* streeet, int number) {
	Person_name = name;
	Street = streeet;
	House = number;

}
void Person::show() {
	cout << "Person's name:" << Person_name << endl;
	cout << "Street:" << Street << endl;
	cout << "Gender:" << House << endl;

}

void Person::view(Person a) {
	a.show();

}
