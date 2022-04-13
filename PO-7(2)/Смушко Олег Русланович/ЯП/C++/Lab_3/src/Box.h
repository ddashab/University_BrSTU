//
// Created by Олег on 04.10.2021.
//

#ifndef LAB_3_BOX_H
#define LAB_3_BOX_H
#include "Figures.h"

class Box: public Figures{
    double a;
public:
    Box(double a);
    void showSquare() override;
    void showPerimeter() override;
    double Read_a();
    bool operator == (const Box& right){  //overloading == operator
        return square == right.square;
    }
    bool operator != (Box *const right){  //overloading != operator
        return this != right;
    }
    Box &operator = (const Box &right){  //overloading = operator
        square = right.square;
        return *this;
    }
};
#endif //LAB_3_BOX_H
