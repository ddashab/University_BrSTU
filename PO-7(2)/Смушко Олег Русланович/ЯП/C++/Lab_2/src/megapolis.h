//
// Created by Олег on 29.09.2021.
//

#ifndef LAB_2_MEGAPOLIS_H
#define LAB_2_MEGAPOLIS_H
#include "place.h"
#include "town.h"

class Megapolis: public Town{
protected:
    int population;
public:
    Megapolis(string name, float square, int population);
    void show();
    void set_population(int population);
    int get_population();
};

#endif //LAB_2_MEGAPOLIS_H
