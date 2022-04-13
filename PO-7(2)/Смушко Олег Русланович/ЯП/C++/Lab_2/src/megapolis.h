//
// Created by Олег on 29.09.2021.
//

#ifndef LAB_2_MEGAPOLIS_H
#define LAB_2_MEGAPOLIS_H
#include "place.h"
#include "town.h"

class Megapolis: public Town{  //Megapolis class declaration
protected:
    int population;
public:
    Megapolis(string name, float square, int population);  //constructor with parameters
    void show();  //redeclaration of the show function
    void set_population(int population);  //set field population
    int get_population();  //to get value of the field population
};

#endif //LAB_2_MEGAPOLIS_H
