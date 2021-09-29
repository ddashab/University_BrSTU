//
// Created by Олег on 29.09.2021.
//

#ifndef LAB_2_REGION_H
#define LAB_2_REGION_H
#include "place.h"

class Region: public Place {
protected:
    int cityCount;
public:
    Region(string name, int cityCount);
    void show();
    void set_count(int cityCount);
    int get_count();
};

#endif //LAB_2_REGION_H
