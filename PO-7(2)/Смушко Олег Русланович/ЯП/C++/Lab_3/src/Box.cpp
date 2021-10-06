//
// Created by Олег on 04.10.2021.
//

#include "Box.h"
Box::Box(double a){  //constructor with parameters
    square = a * a;
    perimeter = 4 * a;
}

double Box::Read_a() {  //entering a value
    cout << "Enter side of the square: ";
    cin >> a;
    return a;
}

void Box::showSquare() {  //display square value
    cout << "Square of box: " << square << endl;
}

void Box::showPerimeter() {  //display perimeter value
    cout << "Perimeter of box: " << perimeter << endl;
}
