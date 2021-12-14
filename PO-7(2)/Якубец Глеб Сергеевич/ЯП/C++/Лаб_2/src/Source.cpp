//                 .-> Ðåñïóáëèêà
//  Ãîñóäàðñòâî   /-> Ìîíàðõèÿ -> Êîðîëåâñòâî
//

#include "Classes.h"

int main() {
	setlocale(LC_ALL, "rus");
	Monarchy a1 = Monarchy("Êàçàõñòàí", 12, 10, nullptr, "Ïàðëàìåíòñêàÿ", 24, 8);
	Republic a2 = Republic("Áåëàðóñü", 16, 15, nullptr, 2.86, "Ïðåçèäåíòñêàÿ");
	Kingdom a3 = Kingdom("Èñïàíèÿ", 14, 48, nullptr, "Àáñîëþòíîå", 49, 4, "Çîëîòàÿ ñ ñàïôèðàìè");
	State::show_list();



	return 0;
}
