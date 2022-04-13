#include "express .h"


express::express() :train() {}

express::express(char* type, int weight, char* kind, char* otkuda, char* kuda) {
		this->type = type;
		this->weight = weight;
		this->kind = kind;
		this->otkuda = otkuda;
		this->kuda = kuda;
	}
void express::expres_set(char* type, int weight, char* kind, char* otkuda, char* kuda) {
		this->type = type;
		this->weight = weight;
		this->kind = kind;
		this->otkuda = otkuda;
		this->kuda = kuda;
	}

void express::show() {
		cout << "Тип: " << type << endl;
		cout << "Вес: " << weight << endl;
		cout << "Вид: " << kind << endl;
		cout << "Откуда отправляется: " << otkuda << endl;
		cout << "Куда прибывает: " << kuda << endl;

	}

express::~express() {}
