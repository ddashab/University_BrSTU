#include "Product.h"

Product::Product() :  //реализация конструктора без параметров
	name("Bread"), amount(3), cost(45.99)
{
	cout << "Constructor without parameters called for Product: " << name << endl;
}

Product::Product(string name_, int amount_, float cost_) :  //реализация конструктора с параметрами
	name(name_), amount(amount_), cost(cost_)
{
	cout << "Constructor with parameters called for Product: " << name << endl;
}

Product::~Product() {  //реализация деструктора
	cout << "Destructor called for Product: " << name << endl;
}

Product::Product(const Product&prod):  //реализация конструктора копирования
	name(prod.name), amount(prod.amount), cost(prod.cost)
{
	cout << "Copying was there." << endl;
}

void Product::print() {  //реализация функции вывода информации полей экземпляра класса в консоль
	cout << "Name: " << name << "; Amount: " << amount << "; Cost: " << cost << endl;
}

void Product::setName(string name_) {  //реализация функции установки значения поля name
	name = name_;
}

void Product::setAmount(int amount_) {  //реализация функции установки значения поля amount
	amount = amount_;
}

void Product::setCost(float cost_) {  //реализация функции установки значения поля cost
	cost = cost_;
}
