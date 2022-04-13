//
// Created by ASUS on 15.10.2021.
//

#ifndef LAB_1_CAR_H
#define LAB_1_CAR_H
#pragma once
#include <iostream>
using namespace std;

class car {
    string name;
    int horsepower;
    float cost;
public:
    car();//конструктор без параметров
    car(string name_n, int horsepower_rr, float cost_s);//конструктор с параметрами
    car(const car& copy_car);
    ~car();//диструктор
    void print();//компоненьы вывода полей
    void set(string name_n, int horsepower_rr, float cost_s);//компоненты установки полей
    void setname(string name_n);//компонента установки поля имя
    void setpower(int horsepower_rr);//компонента установки поля мощность
    void setcost(float cost_s);//компонента установки поля цена
    string getname() {
        return name;
    }
    int gethorsepower() {
        return horsepower;
    }
    float getcost() {
        return cost;
    }
};
#endif //LAB_1_CAR_H
