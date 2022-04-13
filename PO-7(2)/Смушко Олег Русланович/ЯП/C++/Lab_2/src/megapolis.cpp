//
// Created by Олег on 29.09.2021.
//

#include "megapolis.h"


Megapolis::Megapolis(string name, float square, int population) : Town(name, square){  //defining constructor with parameters
    this->population = population;
}

void Megapolis::show() {  //defining redeclared show function
    cout << endl << "=================================" << endl << "Region name: " << this->name << endl << "Town square: " << this->square << endl << "Megapolis population: " << this->population << endl << "=================================" << endl << endl;
}

void Megapolis::set_population(int population) {  //defining function for setting field population
    this->population = population;
}

int Megapolis::get_population() {  //defining function for getting value of the field population
    return this->population;
}