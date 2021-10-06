//
// Created by Олег on 02.10.2021.
//

#ifndef LAB_3_ELLIPSE_H
#define LAB_3_ELLIPSE_H

#include "Figures.h"

class Ellipse: public Figures{
    double a, b;
public:
    Ellipse(double a, double b);
    void showSquare() override;
    void showPerimeter() override;
    double Read_a();
    double Read_b();
    bool operator == (const Ellipse& right){  //overloading == operator
        return square == right.square;
    }
    bool operator != (Ellipse *const right){  //overloading != operator
        return this != right;
    }
    Ellipse &operator = (const Ellipse &right){  //overloading = operator
        square = right.square;
        return *this;
    }
};

#endif //LAB_3_ELLIPSE_H
