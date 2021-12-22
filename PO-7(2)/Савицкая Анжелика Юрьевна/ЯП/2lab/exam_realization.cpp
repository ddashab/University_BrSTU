#include "exam.h"

Exam::Exam() : Education() {}

Exam::Exam(char* person, int room, int kol) : Education() {

	this->person = person;
	this->room = room;
	this->kol = kol;

}

void Exam::set(char* person, int room, int kol) {

	this->person = person;
	this->room = room;
	this->kol = kol;

}

void Exam::show() {

	cout << "Преподаватель: " << person << endl;
	cout << "Аудитория: " << room << endl;
	cout << "Количество должников: " << kol << endl;

}
Exam::~Exam() {}
