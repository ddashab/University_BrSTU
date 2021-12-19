#include "circle.h"

#include "rectangle.h"

#include "Triangle.h"

#include "operate.h"

using namespace std;

void menu(Operation arr);

int main() {

	setlocale(LC_ALL, "rus");
	Operation arr(0);
	menu(arr);
	system("pause");
	return 0;
}

void menu(Operation arr) {
	bool exit = false;
	while (!exit) {
		cout << "1 - add circle" << endl
			<< "2 - add rectangle" << endl
			<< "3 - add triangle" << endl
			<< "4 - compare rectangle" << endl
			<< "5 - print figure on index" << endl
			<< "6 - print all figures" << endl
			<< "7 - delete from end" << endl
			<< "8 - delete on index" << endl
			<< "0 - exit" << endl;
		try

		{
			int num;
			cin >> num;
			cout << endl;
			switch (num)
			{
			case 1:
			{
				Circle* obj1 = new Circle(0);
				obj1->Read();
				Circle* obj2 = new Circle(0);
				obj2 = obj1;
				bool temp = false;
				cout << "Add in end(0) or on index(1)?";
				cin >> temp;
				if (temp) {
					int index;
					cout << "Input index: ";
					cin >> index;
					arr.Add(index, obj2);
				}
				else {
					arr.AddEnd(obj2);
				}
				break;
			}
			case 2:
			{
				Rectangle* obj = new Rectangle(0, 0);
				obj->Read();
				bool temp = false;
				cout << "Add in end(0) or on index(1)?";
				cin >> temp;
				if (temp) {
					int index;
					cout << "Input index: ";
					cin >> index;
					arr.Add(index, obj);
				}
				else {
					arr.AddEnd(obj);
				}
				break;
			}
			case 3:
			{
				Triangle* obj = new Triangle(0, 0, 0, 0);
				obj->Read();
				bool temp = false;
				cout << "Add in end(0) or on index(1)?";
				cin >> temp;
				if (temp) {
					int index;
					cout << "Input index: ";
					cin >> index;
					arr.Add(index, obj);
				}
				else {
					arr.AddEnd(obj);
				}
				break;
			}
			case 4:
			{
				Rectangle obj1(0, 0);
				obj1.Read();
				Rectangle obj2(0, 0);
				obj2.Read();
				if (obj1 == obj2) {
					cout << "Figures equals" << endl; 
				}
				else if (obj1 != obj2) {
					cout << "Figures not equals" << endl; 
				}
				break;
			}
			case 5:
			{
				int index;
				cout << "Input index: ";
				cin >> index;
				if (arr[index] != 0) {
					arr[index]->Print();
				}
				break;
			}
			case 6:
			{
				cout << "Number feagures = " << arr.get_a() << endl;
				for (int i = 0; i < arr.get_a(); i++) {
					arr[i]->Print();
				}
				break;
			}
			case 7:
			{
				arr.DeleteEnd();
				break;
			}
			case 8:
			{
				int index;
				cout << "Input index: ";
				cin >> index;
				arr.Delete(index);
				break;
			}
			case 0:
				exit = true;
			}
			cout << endl;
		}
		catch(...)
		{
			cout << "Error" << endl;
		}
	}
}