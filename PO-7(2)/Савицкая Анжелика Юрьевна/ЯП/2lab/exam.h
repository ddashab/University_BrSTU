#pragma once
#include "education.h"

class Exam :public Education {

protected:

	int kol;

public:

	Exam();
	Exam(char* person, int room, int kol);
	void set(char* person, int room, int kol);
	void show();

	~Exam();

};
