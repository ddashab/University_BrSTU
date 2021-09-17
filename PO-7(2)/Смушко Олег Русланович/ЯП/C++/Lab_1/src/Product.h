#ifndef PRODUCT_H
#define PRODUCT_H
#include <iostream>
#include <string>

using namespace std;

class Product {
	string name;
	int amount;
	float cost;

public:
	Product();  //конструктор без параметров
	Product(string name_, int amount_, float cost_);  //конструктор с параметрами
	Product(const Product& prod);  //конструктор копирования
	~Product();  //деструктор
	string get_name() {  //функция для доступа к полю name
		return name;
	}
	int get_amount() {  //функция для доступа к полю amount
		return amount;
	}
	float get_cost() {  //функция для доступа к полю cost
		return cost;
	}
	void print();  //функция вывода содержимого полей экземпляра класса
	void setName(string name_);  //функция для установки значения поля name
	void setAmount(int amount_);  //функция для установки значения поля amount
	void setCost(float cost_);  //функция для установки значения поля cost
};
#endif PRODUCT_H