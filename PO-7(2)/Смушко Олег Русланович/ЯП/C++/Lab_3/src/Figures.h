//
// Created by Олег on 02.10.2021.
//

#ifndef LAB_3_FIGURES_H
#define LAB_3_FIGURES_H

#include <iostream>
#include <locale>
#define pi 3.14159
using namespace std;

class Figures{  //abstract class
protected:
    double square;
    double perimeter;
public:
    double get_square() const{  //getting square value
        return square;
    }
    double get_perimeter() const{  //getting perimeter value
        return perimeter;
    }
    virtual void showSquare() = 0;  //pure virtual function for displaying square value
    virtual void showPerimeter() = 0;  //pure virtual function for displaying perimeter value
};


#endif //LAB_3_FIGURES_H
