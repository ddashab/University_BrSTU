//
// Created by Олег on 29.09.2021.
//

#include "town.h"

Town::Town(string name, float square) : Place(name){
    this->square = square;
}

void Town::show(){
    cout << "=================================" << endl << "Region name: " << this->name << endl << "Town square: " << this->square << endl<< "=================================" << endl << endl;
}

void Town::set_square(float square) {
    this->square = square;
}

float Town::get_square() {
    return this->square;
}