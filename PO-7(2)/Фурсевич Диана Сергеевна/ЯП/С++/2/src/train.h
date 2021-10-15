#pragma once
#include "transport_means.h"

class train : public transport_means { //класс поезд

protected:
	char* kind; // 

public:
	train();
	train(char* type, int weight, char* kind);
	void train_set(char* type, int weight, char* kind);
	void show() override;
	~train();
};