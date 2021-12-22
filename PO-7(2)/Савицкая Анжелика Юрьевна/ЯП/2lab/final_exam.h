#pragma once
#include "exam.h"

class Final_exam :public Exam {

protected:

	int time;

public:

	Final_exam();
	Final_exam(char* person, int room, int kol, int time);
	void set(char* person, int room, int kol, int time);
	void show();
	~Final_exam();

};
#pragma once
