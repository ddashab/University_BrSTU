//
// Created by Олег on 29.09.2021.
//

#include "region.h"

Region::Region(string name, int cityCount) : Place(name) {
    this->cityCount = cityCount;
}

void Region::show(){
    cout << "=================================" << endl << "Region name: " << this->name << endl << "City count: " << this->cityCount << endl<< "=================================" << endl << endl;
}

void Region::set_count(int cityCount) {
    this->cityCount = cityCount;
}

int Region::get_count() {
    return this->cityCount;
}
