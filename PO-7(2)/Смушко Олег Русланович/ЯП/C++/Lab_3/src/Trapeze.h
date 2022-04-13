//
// Created by Олег on 04.10.2021.
//

#ifndef LAB_3_TRAPEZE_H
#define LAB_3_TRAPEZE_H
#include "Figures.h"

class Trapeze: public Figures{
    double a, b, c, d, h;
public:
    Trapeze(double a, double b, double c, double d, double h);
    void showSquare() override;
    void showPerimeter() override;
    double Read_a();
    double Read_b();
    double Read_c();
    double Read_d();
    double Read_h();
    bool operator == (const Trapeze& right){  //overloading == operator
        return square == right.square;
    }
    bool operator != (Trapeze *const right){  //overloading != operator
        return this != right;
    }
    Trapeze &operator = (const Trapeze &right){  //overloading = operator
        square = right.square;
        return *this;
    }
};
#endif //LAB_3_TRAPEZE_H
