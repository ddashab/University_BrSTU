#include "triangle.h"

Triangle::Triangle() {}
Triangle::Triangle(int a, int b, int c, int h) {
	this->a = a;
	this->b = b;
	this->c = c;
	this->h = h;
}

Triangle::Triangle(const Triangle& cn) {
	a = cn.a;
	b = cn.b;
	c = cn.c;
	h = cn.h;
}

Triangle::~Triangle() {}
bool Triangle::operator == (const Triangle& op) {
	return (a == op.a) && (b == op.b) && (c == op.c) && (h == op.h);
}

bool Triangle::operator != (const Triangle& op) {
	return !(*this == op);
}

Triangle& Triangle::operator = (const Triangle& op) {
	a = op.a;
	b = op.b;
	c = op.c;
	h = op.h;
	return *this;
}

void Triangle::Print() {
	cout << endl << "Triangle: " << "a= " << a << ", b= " << b << ", c= " << c << ", h= " << h << endl;
	cout << "Square: " << "S= " << Square() << endl;
	cout << "Perimeter: " << "P= " << Perimetr() << endl;
}

void Triangle::Read() {
	cout << endl << "Enter first side of the triangle: ";
	cin >> a;
	cout << "Enter second side of the triangle: ";
	cin >> b;
	cout << "Enter the base of the triangle: ";
	cin >> c;
	cout << "Enter the height of the triangle: ";
	cin >> h;
}

double Triangle::Perimetr() {
	return (a + b + c);
}

double Triangle::Square() {
	return (c * h) / 2;
}