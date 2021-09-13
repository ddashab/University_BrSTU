#ifndef LAB1_WORKSHOP_H
#define LAB1_WORKSHOP_H
#pragma once
#include <iostream>
using namespace std;
class workshop {
    string name;
    string chief;
    int number;
public:
    workshop();
    workshop(string n_name, string c_chief, int n_number);//конструктор с параметрами
    workshop(const workshop &copy_workshop);
    ~workshop();
    void Show();
    void setName(string new_name);
    void setChief(string new_chief);
    void setNumber(int new_number);
    string getName();
    string getChief();
    int getNumber();
};
#endif //LAB1_WORKSHOP_H
