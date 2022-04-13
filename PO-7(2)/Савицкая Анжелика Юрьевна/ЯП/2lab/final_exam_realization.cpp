#include "final_exam.h"

Final_exam::Final_exam() : Exam() {}

Final_exam::Final_exam(char* person, int room, int kol, int time) : Exam(person, room, kol) {

	this->person = person;
	this->room = room;
	this->kol = kol;
	this->time = time;

}

void Final_exam::set(char* person, int room, int kol, int time) {

	this->person = person;
	this->room = room;
	this->kol = kol;
	this->time = time;

}

void Final_exam::show() {

	cout << "Преподаватель: " << person << endl;
	cout << "Аудитория: " << room << endl;
	cout << "Количество должников: " << kol << endl;
	cout << "Длительность(в академических часах): " << time << endl;

}

Final_exam::~Final_exam() {}
