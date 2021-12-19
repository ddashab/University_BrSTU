#pragma once

#include "figur.h"

class Operation {
private:
	Figures** arr;
	int a;
public:
	Operation(int a);
	~Operation();
	Figures* operator[] (int n) const;
	Figures*& operator[] (int n);
	int get_a();
	void AddEnd(Figures* figure);
	void Add(int index, Figures* figure);
	void DeleteEnd();
	void Delete(int index);
};