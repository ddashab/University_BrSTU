#pragma once
#include <iostream>
#include <Windows.h>
using namespace std;

class transport_means { // класс транспортное средство

protected:
	char* type; //тип
	int weight; // вес

public:
	transport_means();
	void add();
	virtual void show() = 0; // чистая виртуальная функция 
	static transport_means* head; //указатель на начало связного списка
	transport_means* next;
	static void show_list(); //для просмотр списка
	~transport_means();
};