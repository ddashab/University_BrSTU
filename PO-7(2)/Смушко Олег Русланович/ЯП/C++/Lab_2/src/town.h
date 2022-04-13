//
// Created by Олег on 29.09.2021.
//

#ifndef LAB_2_TOWN_H
#define LAB_2_TOWN_H
#include "place.h"

class Town : public Place{  //Town class declaration
protected:
    float square;
public:
    Town(string name, float square);  //constructor with parameters
    void show();  //redeclaration of the show function
    void set_square(float square);  //set field square
    float get_square();  //to get value of the field square
};

#endif //LAB_2_TOWN_H
