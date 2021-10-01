#pragma once
#include <iostream>

using namespace std;

class Person {

private:

	char* m_name; //имя (указатель на текстовую строку)
	int m_age; //возраст
	int m_floor; //пол

public:

	Person(); //конструктор без параметров 
	Person(char* name, int age, int floor); //конструктор с параметрами
	Person(const Person &other); //конструктор копирования
	~Person(); //деструктор

	// для просмотра и установки полей данных
	char* GETName();  //для получения значений поля имя
	int GETAge(); //для получения значений поля возраст
	int GETFloor(); //для получения значений поля пол
	void SETName(char* name); //для установки значений поля имя
	void SETAge(int age); //для установки значений поля возраст
	void SETFloor(int floor); //для установки значений поля пол
	void SET(char* name, int age, int floor); // инициализация всех полей объекта
	void Show(); //просомтр полей объекта
	void View(Person);


};
