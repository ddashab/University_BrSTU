//
// Created by Олег on 29.09.2021.
//

#include "region.h"

Region::Region(string name, int cityCount) : Place(name) {  //defining constructor with parameters
    this->cityCount = cityCount;
}

void Region::show(){  //defining redeclared show function
    cout << "=================================" << endl << "Region name: " << this->name << endl << "City count: " << this->cityCount << endl<< "=================================" << endl << endl;
}

void Region::set_count(int cityCount) {  //defining function for setting field cityCount
    this->cityCount = cityCount;
}

int Region::get_count() {  //defining function for getting value of the field CityCount
    return this->cityCount;
}
