#include "Class.h"

int main() {
	setlocale(LC_ALL, "rus");
	string x = "Месопотамия";
	string y = "Монархия";
	float z = 1565.54;
	State f1(x, y, z);
	State* f2 = new State();
	void(State:: * ptr)();
	ptr = &State::show;
	(f1.*ptr)();
	(f2->*ptr)();
	delete f2;
	return 0;
}