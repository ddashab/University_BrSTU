#pragma once
#include "Software_Errors.h"
#include "error.h"
class sSoftware_Errors {
private:
	Software_Errors** arr;
	int count;
public:
	sSoftware_Errors(int count);
	~sSoftware_Errors();
	Software_Errors* operator[] (int n) const;
	Software_Errors*& operator[] (int n);
	int get_count();
	void addToTheEnd(Software_Errors* figure);
	void add(int index, Software_Errors* figure);
	void deleteFromTheEnd();
	void del(int index);
};
