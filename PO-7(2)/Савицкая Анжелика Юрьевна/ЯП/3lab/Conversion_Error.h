#pragma once
#include "Software_Errors.h"
class Conversion_Error :public Software_Errors {
private:
	int pop;
public:
	Conversion_Error();
	Conversion_Error(int pop);
	Conversion_Error(const Conversion_Error& other);
	~Conversion_Error();
	bool operator == (const Conversion_Error& right);
	bool operator != (const Conversion_Error& right);
	Conversion_Error& operator = (const Conversion_Error& right);
	void Print();
	void Read();
};
