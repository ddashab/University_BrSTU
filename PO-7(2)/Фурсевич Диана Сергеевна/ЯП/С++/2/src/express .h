#pragma once
#include "train.h"

class express : public train {// класс экспресс

protected:
	char* otkuda;
	char* kuda;

public:
	express();
	express(char* type, int weight, char* kind, char* otkuda, char* kuda);
	void expres_set(char* type, int weight, char* kind, char* otkuda, char* kuda);
	void show() override;
	~express();
};