#pragma once
#include <iostream>

using namespace std;
class Education {

protected:

	char* person;
	int room;
	virtual void show() = 0;

public:

	Education();
	static Education* head; //указатель на начало связанного списка объектов
	Education* next;
	void add();
	//статическая функция для просмотра списка
	static void look_up_list();
	virtual~Education();
};
#pragma once
