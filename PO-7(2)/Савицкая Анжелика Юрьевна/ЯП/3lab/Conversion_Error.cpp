#include "Conversion_Error.h"
Conversion_Error::Conversion_Error() {}
Conversion_Error::Conversion_Error(int pop) {
	this->pop = pop;
}
Conversion_Error::Conversion_Error(const Conversion_Error& other) {
	pop = other.pop;
}
Conversion_Error::~Conversion_Error() {}
bool Conversion_Error::operator == (const Conversion_Error& right) {
	return (pop == right.pop);
}
bool Conversion_Error::operator != (const Conversion_Error & right) {
	return !(*this == right);
}
Conversion_Error& Conversion_Error::operator = (const Conversion_Error & right) {
	pop = right.pop;
	return *this;
}
void Conversion_Error::Print() {
	cout << "Ошибка - ошибка преобразования" << endl << "Количестов попыток 	устранения ошибки:" << pop << endl;
}
void Conversion_Error::Read() {
	cout << "Введите количестов попыток устранения ошибки: ";
	cin >> pop;
}
