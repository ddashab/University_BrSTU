#include"car.h"

int main() {
    setlocale(0, "");
    car first;
    car second("Porsche Taycan", 761, 186.991);
    car third(second);
    car *set_cost = new car;

    car *set_name = new car;
    car *set_horse = new car;

    set_name->setname("Something");
    set_horse->setpower(777);
    set_cost->setcost(12.7);

    set_name->print();
    set_horse->print();
    set_cost->print();

    delete(set_name);
    delete(set_horse);
    delete(set_cost);

    first.print();
    second.print();
    third.print();
    third.set("Audi etron", 408, 101.869);
    third.print();
}