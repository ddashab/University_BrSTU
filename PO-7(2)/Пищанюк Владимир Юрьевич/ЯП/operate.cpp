#include "operate.h"

Operation::Operation(int a) {
	arr = new Figures * [a];
	for (int i = 0; i < a; i++) {
		arr[i] = nullptr;
	}
	this->a = a;

}

Operation::~Operation() {
	for (int i = 0; i < a; i++) {
		if (arr[i] != nullptr) {
			delete arr[i];
		}
		delete[]arr;
	}
}

Figures* Operation::operator[] (int n) const {
	return arr[n];
}

Figures*& Operation::operator[] (int n) {
	return arr[n];
}

int Operation::get_a() {
	return a;
}

void Operation::AddEnd(Figures* figure) {
	Figures** temp = new Figures * [a + 1];
	for (int i = 0; i < a; i++) {
		temp[i] = arr[i];
}
	arr = temp;
	temp[a] = figure;
	a++;
}

void Operation::Add(int index, Figures* figure) {
	Figures** temp = new Figures * [a + 1];
	for (int i = 0; i < index; i++) {
		temp[i] = arr[i];
	}
	temp[index] = figure;
	for (int i = index; i < a; i++) {
		temp[i + 1] = arr[i];
	}
	arr = temp;
	a++;
}

void Operation::DeleteEnd() {
	Figures** temp = new Figures * [a - 1];
	for (int i = 0; i < a - 1; i++) {
		temp[i] = arr[i];
	}
	arr = temp;
	a--;
}

void Operation::Delete(int index) {
	Figures** temp = new Figures * [a - 1];
	for (int i = 0; i < index; i++) {
		temp[i] = arr[i];
	}
	for (int i = index + 1; i < a; i++) {
		temp[i - 1] = arr[i];
	}
	arr = temp;
	a--;
}