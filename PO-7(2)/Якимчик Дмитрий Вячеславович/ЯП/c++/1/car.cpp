//
// Created by ASUS on 15.10.2021.
//

#include"car.h"

car::car() :
        name("Tesla Model S Plaid"), horsepower(1034), cost(129.991) {
    cout << "The best car in the world is: " << name << "\nwith horse power: " << horsepower << "\nprice: " << cost << endl << endl;
}

car::car(string name_n, int horsepower_rr, float cost_s) :
        name(name_n), horsepower(horsepower_rr), cost(cost_s) {
    cout << "Constructor with parameters for: " << name << endl << endl;
}

car::car(const car& copy_car) :
        name(copy_car.name), horsepower(copy_car.horsepower), cost(copy_car.cost) {
    cout << "Copy for: " << name << endl << endl;
}

car::~car() {
    cout << "Destructor for: " << name << endl << endl;
}

void car::print() {
    cout << "Name: " << name << "\tHorsepower: " << horsepower << "\tPrice: " << cost << endl << endl;
}

void car::set(string name_n, int horsepower_rr, float cost_s){
    name = name_n;
    horsepower = horsepower_rr;
    cost = cost_s;
}

void car::setname(string name_n){
    name = name_n;
}

void car::setpower(int horsepower_rr){
    horsepower = horsepower_rr;
}

void car::setcost(float cost_s){
    cost = cost_s;
}