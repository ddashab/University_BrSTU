//                 .-> Республика
//  Государство   /-> Монархия -> Королевство
//

#include "Classes.h"

int main() {
	setlocale(LC_ALL, "rus");
	Monarchy a1 = Monarchy("Казахстан", 12, 10, nullptr, "Парламентская", 24, 8);
	Republic a2 = Republic("Беларусь", 16, 15, nullptr, 2.86, "Президентская");
	Kingdom a3 = Kingdom("Испания", 14, 48, nullptr, "Абсолютное", 49, 4, "Золотая с сапфирами");
	State::show_list();



	return 0;
}