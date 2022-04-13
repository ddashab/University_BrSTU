#pragma once
#include "figur.h"

class Rectangle :public Figures {
private:
	int a, b;
public:
	Rectangle();
	Rectangle(int a, int b);
	Rectangle(const Rectangle& cn);
	~Rectangle();
	bool operator == (const Rectangle& op);
	bool operator != (const Rectangle& op);
	Rectangle& operator = (const Rectangle& op);
	void Print();
	void Read();
	double Perimetr();
	double Square();
};