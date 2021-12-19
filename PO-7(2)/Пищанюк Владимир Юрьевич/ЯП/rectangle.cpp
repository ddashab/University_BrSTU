#include "rectangle.h"

Rectangle::Rectangle() {}
Rectangle::Rectangle(int a, int b) {
	this->a = a;
	this->b = b;
}
Rectangle::Rectangle(const Rectangle& cn) {
	a = cn.a;
	b = cn.b;
}
Rectangle::~Rectangle() {}

bool Rectangle::operator == (const Rectangle& op) {
	return (a == op.a) && (b == op.b);
}
bool Rectangle::operator != (const Rectangle& op) {
	return !(*this == op);
}
Rectangle& Rectangle::operator = (const Rectangle& op) {
	a = op.a;
	b = op.b;
	return *this;
}
void Rectangle::Print() {
	cout << endl << "Rectangle: " << "a=" << a << ", b=" << b << endl;
	cout << "Square: " << "S=" << Square() << endl;
	cout << "Perimeter: " << "P=" << Perimetr() << endl;
}
void Rectangle::Read() {
	cout << endl << "Enter the length of the rectangle: ";
	cin >> a;
	cout << "Enter the width of the rectangle: ";
	cin >> b;
}
double Rectangle::Perimetr() {
	return 2 * (a + b);
}
double Rectangle::Square() {
	return  (a * b);
}
