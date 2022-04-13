#include "transport_means.h"

transport_means* transport_means::head = 0;
transport_means::transport_means()
	{
		add();
	}
void transport_means::add() 
	{
		transport_means* new_tr = this;
		new_tr->next = head;
		head = new_tr;
	}
void transport_means::show() {}

void transport_means::show_list() { //для просмотр списка
		transport_means* new_tr = head;
		cout << "Список: " << endl;
		while (new_tr) {
			new_tr->show();
			cout << "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _"<<endl;
			new_tr = new_tr->next;
		}
	}
transport_means ::~transport_means() {}
