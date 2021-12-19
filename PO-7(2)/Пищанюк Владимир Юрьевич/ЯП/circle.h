#define _USE_MATH_DEFINES

#include "figur.h"

class Circle :public Figures {
private:
	int R;
public:
	Circle();
	Circle(int R);
	Circle(const Circle& n);
	~Circle();
	bool operator == (const Circle& op);
	bool operator != (const Circle& op);
	Circle& operator = (const Circle& op);
	void Print();
	void Read();
	double Perimetr();
	double Square();
}; 
#pragma once
