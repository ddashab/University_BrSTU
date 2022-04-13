//
// Created by Олег on 02.10.2021.
//

#include "Ellipse.h"
Ellipse::Ellipse(double a, double b) {  //constructor with parameters
    square = pi * a * b;
    perimeter = 4 * ((pi*a*b + (a-b)*(a-b) / (a+b)));
}

double Ellipse::Read_a() {  //entering a value
    cout << "Enter small semi-axis (a): ";
    cin >> a;
    return a;
}

double Ellipse::Read_b() {  //entering b value
    cout << "Enter big semi-axis (b): ";
    cin >> b;
    return b;
}

void Ellipse::showSquare() {  //display square value
    cout << "Square of ellipse = " << square << endl;
}

void Ellipse::showPerimeter() {  //display perimeter value
    cout << "Perimeter of ellipse = " << perimeter << endl;
}