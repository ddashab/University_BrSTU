#include "circle.h"
#include "math.h"

Circle::Circle() {}
Circle::Circle(int R) {
	this->R = R;
}
Circle::Circle(const Circle& cn) {
	R = cn.R;
}
Circle::~Circle() {}

bool Circle::operator == (const Circle& op) {
	return R == op.R;
}

bool Circle::operator != (const Circle& op) {
	return !(*this == op);
}

Circle& Circle::operator = (const Circle& op) {
	R = op.R;
	return *this;
}

void Circle::Print() {
	cout << endl << "A circle: " << "R= " << R << endl;
	cout << "Square: " << "S= " << Square() << endl;
	cout << "Perimeter: " << "P= " << Perimetr() << endl;
}

void Circle::Read() {
	cout << endl << "Enter the radius of the circle: ";
	cin >> R;
}

double Circle::Perimetr() {
	return 2 * M_PI * R;
}

double Circle::Square() {
	return 2 * M_PI * pow(R, 2);
}