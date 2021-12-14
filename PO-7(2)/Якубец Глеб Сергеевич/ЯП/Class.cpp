#include "Class.h"

State::State() {
	name = "Неверленд";
	form = "Без власти";
	area = 10000.43;
	cout << "Конструктор без параметров вызван для объекта " << this << endl;
}

State::State(string nm, string frm, float ar) {
	name = nm;
	form = frm;
	area = ar;
	cout << "Конструктор вызван для объекта " << this << endl;
}

void State::set_name(string nm) {
		name = nm;
}

void State::set_form(string frm) {
		form = frm;
}

void State::set_area(float ar) {
		area = ar;
}

void State::read() {
	cout << "Введите название гос-ва" << endl;
	cin >> name;
	cout << "Укажите форму правления" << endl;
	cin >> form;
	cout << "Введите площадь" << endl;
	cin >> area;
}

void State::show() {
	cout << "Описание объекта " << this << endl << "Hазвание: " << name << endl << "Форма правления: " << form << endl << "Площадь: " << area << endl;
}

State::~State() {
	cout << "Страна " << name << " уничтожена! Ахахахахах" << endl;
}

State::State(const State&) {
	cout << "Данные скопированы";
}