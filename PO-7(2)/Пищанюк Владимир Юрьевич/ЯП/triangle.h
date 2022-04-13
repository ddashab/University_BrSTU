#pragma once

#include "figur.h"

class Triangle :public Figures {
private:
	int a, b, c, h;
public:
	Triangle();
	Triangle(int a, int b, int c, int h);
	Triangle(const Triangle& cn);
	~Triangle();
	bool operator == (const Triangle& op);
	bool operator != (const Triangle& op);
	Triangle& operator = (const Triangle& op);
	void Print();
	void Read();
	double Perimetr();
	double Square();
};