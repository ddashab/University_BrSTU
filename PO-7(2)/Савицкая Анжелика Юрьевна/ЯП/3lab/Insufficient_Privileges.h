#pragma once
#include "Software_Errors.h"
class Insufficient_Privileges :public Software_Errors {
private:
	int kol_errors;
public:
	Insufficient_Privileges();
	Insufficient_Privileges(int kol_errors);
	Insufficient_Privileges(const Insufficient_Privileges& other);
	~Insufficient_Privileges();

	bool operator == (const Insufficient_Privileges& right);
	bool operator != (const Insufficient_Privileges& right);
	Insufficient_Privileges& operator = (const Insufficient_Privileges& right);

	void Print();
	void Read();
};
