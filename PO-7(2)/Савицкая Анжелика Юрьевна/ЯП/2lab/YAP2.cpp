#include "education.h"

Education* Education::head = NULL;

Education::Education() {
	add();
}

void Education::show() {
	cout << "на месте виртуальной функции вывожу это" << endl;
}

void Education::add() {

	Education* p = this;
	p->next = head;
	head = p;
}

void Education::look_up_list() {

	Education* p = head;
	cout << "Список: " << "\n";
	while (p) {

		cout << "\n";
		p->show();
		p = p->next;
	}
}

Education::~Education() {}
