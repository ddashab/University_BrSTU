//
// Created by Олег on 29.09.2021.
//

#ifndef LAB_2_PLACE_H
#define LAB_2_PLACE_H

#include <iostream>
#include <string>
#include <list>

using namespace std;

class Place{  //Abstract class Place declaration
protected:
    string name;
public:
    Place(string name);  //constructor with parameters
    virtual void show() = 0;  //Clear virtual function for display list
};
#endif //LAB_2_PLACE_H
