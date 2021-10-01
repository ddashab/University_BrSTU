#include "class.h"

Person::Person() //конструктор по умолчанию 
{
	cout << "Вызвался конструктор без параметров для объекта " << this << endl;

}

Person::Person(char* name, int age, int floor) // прямая инициализация переменных-члена класса
{
	m_name = name;
	m_age = age;
	m_floor = floor;
	cout << "Вызвался конструктор с параметрами для объекта " << this << endl;
}

Person::Person(const Person &other) { //конструктор копирования
	m_name = new char[100];
	m_name = other.m_name;
	m_age = other.m_age;
	m_floor = other.m_floor;
	cout << "Конструктор копирования " << this << endl;
}


Person:: ~Person() {  //деструктор
	cout << "Вызвался деструктор для объекта " << this << endl;
}

char* Person::GETName() { //для получения значений поля имя
	return m_name;
}

int Person::GETAge() { //для получения значений поля возраст
	return m_age;
}


int Person::GETFloor() { //для получения значений поля пол
	return m_floor;
}

void Person::SETName(char* name) { //для установки значений поля имя
	m_name = name;
}

void Person::SETAge(int age) { //для установки значений поля возраст
	m_age = age;
}

void Person::SETFloor(int floor) { //для установки значений поля пол
	m_floor = floor;
}


void Person::SET(char* name, int age, int floor) { // инициализация всех полей объекта
	m_name = name;
	m_age = age;
	m_floor = floor;
}



void Person::Show() { //просмотр полей объекта
	cout << "Имя человека " << m_name << endl;
	cout << "Возраст " << m_age << endl;
	cout << "Пол " << m_floor << endl << endl;
}

void Person::View(Person a) {
	a.Show();
}