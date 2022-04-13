//
// Created by Олег on 29.09.2021.
//

#include "town.h"

Town::Town(string name, float square) : Place(name){  //defining constructor with parameters
    this->square = square;
}

void Town::show(){  //defining redeclared show function
    cout << "=================================" << endl << "Region name: " << this->name << endl << "Town square: " << this->square << endl<< "=================================" << endl << endl;
}

void Town::set_square(float square) {  //defining function for setting field square
    this->square = square;
}

float Town::get_square() {  //defining function for getting value of the field square
    return this->square;
}