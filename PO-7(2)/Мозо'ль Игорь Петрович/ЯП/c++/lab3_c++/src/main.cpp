#include "figures.h"

int main() {
    Figures obj;

    Sphere* a1 = new Sphere(6);
    obj.add(a1);

    Sphere* a2 = new Sphere(5);
    obj.add(a2);

    a1->print();
    a2->print();

    Conus * a3 = new Conus(3, 4, 5);
    obj.add(a3);
    a3->print();

    Pyramid* a4 = new Pyramid(5, 20);
    obj.add(a4);
    a4->print();

    a1->setVolume(500);
    a4->setVolume(500);

    if (*a1 == *a4){
        std::cout << "cool"<<std::endl;
    }
    a2->setVolume(400);
    if (*a2 != *a1) {
        std::cout << "not cool" << std::endl;
    }

    *a1 = *a3;
    a1->print();
    std::cout <<std::endl;
    for(int i = 0; i < obj.getlength(); i++){
        obj[i]->print();
    }
}
