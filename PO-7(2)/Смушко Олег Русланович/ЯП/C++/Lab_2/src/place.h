//
// Created by Олег on 29.09.2021.
//

#ifndef LAB_2_PLACE_H
#define LAB_2_PLACE_H

#include <iostream>
#include <string>
#include <list>

using namespace std;

class Place{
protected:
    string name;
public:
    Place(string name);
    virtual void show() = 0;
};
#endif //LAB_2_PLACE_H
