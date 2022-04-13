#include "transport_means.h"
#include "car.h"
#include "train.h"
#include "express .h"


int main()
{
	SetConsoleCP(1251);
	SetConsoleOutputCP(1251);

	char* type = new char[100];
	cin.getline(type, 100);
	char* mark = new char[100];
	cin.getline(mark, 100);
	car element_1(type, 35, mark);
	car n = element_1;
	n.add(); //элемент сам себя добавляет в список
	element_1.show();
	cout << endl;

	
	type = new char[100];
	cin.getline(type, 100);
	char* kind = new char[100];
	cin.getline(kind, 100);
	train *element_2 = new train(); //включение объекта в список при создании объекта
	element_2->train_set(type, 40, kind);
	element_2->show();
	cout << endl;


	type = new char[100];
	cin.getline(type, 100);
	kind = new char[100];
	cin.getline(kind, 100);
	char* otkuda = new char[100];
	cin.getline(otkuda, 100);
	char* kuda = new char[100];
	cin.getline(kuda, 100);

	express element_3 = express();
	element_3.expres_set(type, 40, kind, otkuda, kuda);
	element_3.show();
	cout << endl;


	transport_means::show_list();

	delete[] type;
	delete[] kind;
	delete[] mark;
	delete[] otkuda;
	delete[] kuda;
	system("pause");
	return 0;
   
}

