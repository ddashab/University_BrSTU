#include "Insufficient_Privileges.h"
Insufficient_Privileges::Insufficient_Privileges() {}
Insufficient_Privileges::Insufficient_Privileges(int kol_errors) {
	this->kol_errors = kol_errors;
}
Insufficient_Privileges::Insufficient_Privileges(const Insufficient_Privileges& other) {
	kol_errors = other.kol_errors;
}
Insufficient_Privileges::~Insufficient_Privileges() {}
bool Insufficient_Privileges::operator == (const Insufficient_Privileges& right) {
	return (kol_errors == right.kol_errors);
}
bool Insufficient_Privileges::operator != (const Insufficient_Privileges & right) {
	return !(*this == right);
}
Insufficient_Privileges& Insufficient_Privileges::operator = (const 	Insufficient_Privileges & right) {
	kol_errors = right.kol_errors;
	return *this;
}
void Insufficient_Privileges::Print() {
	cout << "Ошибка - ошибка недостатка привелегий" << endl << "Количество ошибок:" << kol_errors << endl;
}
void Insufficient_Privileges::Read() {
	cout << "Введите количество ошибок: ";
	cin >> kol_errors;
}
