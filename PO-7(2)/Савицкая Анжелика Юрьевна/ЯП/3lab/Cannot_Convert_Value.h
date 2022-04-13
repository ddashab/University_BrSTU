#pragma once
#include "Software_Errors.h"
class Cannot_Convert_Value :public Software_Errors {
private:
	int dif;
public:
	Cannot_Convert_Value();
	Cannot_Convert_Value(int dif);
	Cannot_Convert_Value(const Cannot_Convert_Value& other);
	~Cannot_Convert_Value();
	bool operator == (const Cannot_Convert_Value& right);
	bool operator != (const Cannot_Convert_Value& right);
	Cannot_Convert_Value& operator = (const Cannot_Convert_Value& right);
	void Print();
	void Read();
};
