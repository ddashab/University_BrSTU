#include "Cannot_Convert_Value.h"
Cannot_Convert_Value::Cannot_Convert_Value() {}
Cannot_Convert_Value::Cannot_Convert_Value(int dif) {
	this->dif = dif;
}
Cannot_Convert_Value::Cannot_Convert_Value(const Cannot_Convert_Value& other) {
	dif = other.dif;
}
Cannot_Convert_Value::~Cannot_Convert_Value() {}
bool Cannot_Convert_Value::operator == (const Cannot_Convert_Value& right) {
	return (dif == right.dif);
}
bool Cannot_Convert_Value::operator != (const Cannot_Convert_Value & right) {
	return !(*this == right);
}
Cannot_Convert_Value& Cannot_Convert_Value::operator = (const Cannot_Convert_Value & right) {
	dif = right.dif;
	return *this;
}
void Cannot_Convert_Value::Print() {
	cout << "Ошибка - невозможно преобразовать значение" << endl << "Сложность ошибки 	(от 0 до 10):" << dif << endl;
}
void Cannot_Convert_Value::Read() {
	cout << "Оцените сложность ошибки (от 0 до 10 ): ";
	cin >> dif;
}
