#include "Class.h"

State::State() {
	name = "Íåâåðëåíä";
	form = "Áåç âëàñòè";
	area = 10000.43;
	cout << "Êîíñòðóêòîð áåç ïàðàìåòðîâ âûçâàí äëÿ îáúåêòà " << this << endl;
}

State::State(string nm, string frm, float ar) {
	name = nm;
	form = frm;
	area = ar;
	cout << "Êîíñòðóêòîð âûçâàí äëÿ îáúåêòà " << this << endl;
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
	cout << "Ââåäèòå íàçâàíèå ãîñ-âà" << endl;
	cin >> name;
	cout << "Óêàæèòå ôîðìó ïðàâëåíèÿ" << endl;
	cin >> form;
	cout << "Ââåäèòå ïëîùàäü" << endl;
	cin >> area;
}

void State::show() {
	cout << "Îïèñàíèå îáúåêòà " << this << endl << "Hàçâàíèå: " << name << endl << "Ôîðìà ïðàâëåíèÿ: " << form << endl << "Ïëîùàäü: " << area << endl;
}

State::~State() {
	cout << "Ñòðàíà " << name << " óíè÷òîæåíà! Àõàõàõàõàõ" << endl;
}

State::State(const State&) {
	cout << "Äàííûå ñêîïèðîâàíû";
}
