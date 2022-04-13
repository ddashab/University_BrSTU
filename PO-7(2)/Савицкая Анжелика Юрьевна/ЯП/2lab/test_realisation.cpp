#include "test.h"

Test::Test() : Education() {}

Test::Test(char* person, int room, int hull) : Education() {

	this->person = person;
	this->room = room;
	this->hull = hull;

}

void Test::set(char* person, int room, int hull) {

	this->person = person;
	this->room = room;
	this->hull = hull;

}

void Test::show() {

	cout << "Преподаватель: " << person << endl;
	cout << "Аудитория: " << room << endl;
	cout << "Корпус: " << hull << endl;

}

Test::~Test() {

}
