//
// Created by Олег on 04.10.2021.
//

#include "Trapeze.h"
//constructor with parameters
Trapeze::Trapeze(double a, double b, double c, double d, double h) {
    square = (h / 2) * a * b;
    perimeter = a + b + c +d;
}

double Trapeze::Read_a() {  //entering a value
    cout << "Enter bigger base: ";
    cin >> a;
    return a;
}

double Trapeze::Read_b() {  //entering b value
    cout << "Enter smaller base: ";
    cin >> b;
    return b;
}

double Trapeze::Read_c() {  //entering c value
    cout << "Enter 1st lateral side: ";
    cin >> c;
    return c;
}

double Trapeze::Read_d() {  //entering d value
    cout << "Enter 2nd lateral side: ";
    cin >> d;
    return d;
}

double Trapeze::Read_h() {  //entering h value
    cout << "Enter height: ";
    cin >> h;
    return h;
}

void Trapeze::showSquare() {  //display square value
    cout << "Square of trapeze: " << square <<  endl;
}

void Trapeze::showPerimeter() {  //display perimeter value
    cout << "Perimeter of trapeze: " << perimeter << endl;
}

