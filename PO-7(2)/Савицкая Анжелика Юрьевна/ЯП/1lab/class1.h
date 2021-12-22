#pragma once
#include <iostream>

using namespace std;

class Person { //по умолчанию private
	char* Person_name;
	char* Street;
	int House;
public:

	Person(); //конструктор без параметров
	Person(char* name, char* streeet, int number); //конструктор с параметрами
	Person(const Person& copyPerson); //конструктор копирования
	~Person(); //деструктор

	void set_name(char* name); //функция для установки значений поля имя
	void set_streeet(char* streeet); //функция для установки значений поля возраст
	void set_number(int number); //функция для установки значений поля пол
	void set(char* name, char* streeet, int number); //функция для установки значений полей
	void show(); //функция для просмотра данных
	void view(Person a); //функция для просмотра данных (нужна, чтобы вызвать констурктор копирования, когда объект передается функции по значению

};
