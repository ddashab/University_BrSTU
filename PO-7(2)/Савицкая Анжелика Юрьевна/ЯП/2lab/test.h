#pragma once
#include "education.h"

class Test : public Education {

protected:

	int hull;

public:

	Test();
	Test(char* person, int room, int hull);
	void set(char* person, int room, int hull);
	void show();
	~Test();

};

