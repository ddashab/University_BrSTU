//
// Created by Олег on 29.09.2021.
//

#ifndef LAB_2_TOWN_H
#define LAB_2_TOWN_H
#include "place.h"

class Town : public Place{
protected:
    float square;
public:
    Town(string name, float square);
    void show();
    void set_square(float square);
    float get_square();
};

#endif //LAB_2_TOWN_H
