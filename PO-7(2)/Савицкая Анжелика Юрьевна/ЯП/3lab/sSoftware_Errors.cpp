#include "sSoftware_Errors.h"
sSoftware_Errors::sSoftware_Errors(int count) {
	arr = new Software_Errors * [count];
	for (int i = 0; i < count; i++) {
		arr[i] = nullptr;
	}
	this->count = count;
}
sSoftware_Errors::~sSoftware_Errors() {
	for (int i = 0; i < count; i++) {
		if (arr[i] != nullptr) {
			delete arr[i];
		}
		delete[]arr;
	}
}
Software_Errors* sSoftware_Errors::operator[] (int n) const {
	if (n < 0 || n >= count) {
		throw IndexError("Вы вышли за границы массива.");
	}
	return arr[n];
}
Software_Errors*& sSoftware_Errors::operator[] (int n) {
	if (n < 0 || n >= count) {
		throw IndexError("Вы вышли за границы массива.");
	}
	return arr[n];
}
int sSoftware_Errors::get_count() {
	return count;
}
void sSoftware_Errors::addToTheEnd(Software_Errors* figure) {
	Software_Errors** temp = new Software_Errors * [count + 1];
	for (int i = 0; i < count; i++) {
		temp[i] = arr[i];
	}
	arr = temp;
	temp[count] = figure;
	count++;
}
void sSoftware_Errors::add(int index, Software_Errors* figure) {
	if (index < 0 || index > count) {
		addToTheEnd(figure);
		throw IndexError("Вы вышли за границы массива. Ошибка будет добавлена в конец массива");
	}
	Software_Errors** temp = new Software_Errors * [count + 1];
	for (int i = 0; i < index; i++) {
		temp[i] = arr[i];
	}
	temp[index] = figure;
	for (int i = index; i < count; i++) {
		temp[i + 1] = arr[i];
	}
	arr = temp;
	count++;
}
void sSoftware_Errors::deleteFromTheEnd() {
	Software_Errors** temp = new Software_Errors * [count - 1];
	for (int i = 0; i < count - 1; i++) {
		temp[i] = arr[i];
	}
	arr = temp;
	count--;
}
void sSoftware_Errors::del(int index) {
	Software_Errors** temp = new Software_Errors * [count - 1];
	for (int i = 0; i < index; i++) {
		temp[i] = arr[i];
	}
	for (int i = index + 1; i < count; i++) {
		temp[i - 1] = arr[i];
	}
	arr = temp;
	count--;
}
