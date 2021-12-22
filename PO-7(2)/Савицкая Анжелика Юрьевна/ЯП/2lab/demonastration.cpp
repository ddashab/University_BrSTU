#include "education.h"
#include "exam.h"
#include "final_exam.h"
#include "test.h"
#include <iostream>

using namespace std;

int main() {

	setlocale(0, "");
	system("color F0");
	char* person = new char[100];
	cin.getline(person, 100);
	Test object1(person, 422, 1);
	Test p = object1;
	p.add(); //объект сам добавляет себя в список
	object1.show();
	cout << endl;
	person = new char[100];
	cin.getline(person, 100);
	int kol;
	cin >> kol;

	Exam* object2 = new Exam(); //включение объекта в список при создании объекта

	object2->set(person, 312, kol);
	object2->show();
	cout << endl;
	person = new char[100];
	cin.ignore();
	cin.getline(person, 100);
	int room;
	cin >> room;
	Final_exam object3 = Final_exam();
	object3.set(person, room, 20, 4);
	object3.show();
	cout << endl;
	Education::look_up_list();
	delete object2;
	delete[] person;
	system("pause");
	return 0;
}
