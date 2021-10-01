//
// Created by Олег on 29.09.2021.
//

#ifndef LAB_2_REGION_H
#define LAB_2_REGION_H
#include "place.h"

class Region: public Place {  //Region class declaration
protected:
    int cityCount;
public:
    Region(string name, int cityCount);  //constructor with parameters
    void show();  //redeclaration of the show function
    void set_count(int cityCount);  //set field cityCount
    int get_count();  //to get value of the field cityCount
};

#endif //LAB_2_REGION_H
