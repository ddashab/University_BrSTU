#include <math.h>
#include "header.h"

double Geometrical_figure::getV() const {
    return V;
}

double Geometrical_figure::getS() const {
    return S;
}
///Cube
void Cube::Show() {
    std::cout << "Cube V = " << V << std::endl;
    std::cout << "Cube S = " << S << std::endl;
}
Cube::Cube(double new_a) :a(new_a) {
    V = pow(new_a, 3);
    S = 6 * pow(new_a, 2);
}

///Cylinder

void Cylinder::Show() {
    std::cout << "Cylinder V = " << V << std::endl;
    std::cout << "Cylinder S = " << S << std::endl;
}
Cylinder::Cylinder(double new_r, double new_h) :r(new_r), h(new_h) {
    V = 3.14 * pow(new_r, 2) * new_h;
    S = (2 * 3.14 * new_h * new_r) + (2 * 3.14 * pow(new_r, 2));
}

///Tetrahedron

void Tetrahedron::Show() {
    std::cout << "Tetrahedron V = " << V << std::endl;
    std::cout << "Tetrahedron S = " << S << std::endl;
}

Tetrahedron::Tetrahedron(double new_a) :_a(new_a) {
    V = (pow(new_a, 3) * sqrt(2)) / 12;
    S = pow(new_a, 2) * sqrt(3);
}

///Arrayptr

void Arrayptr::add(Geometrical_figure* figure) {
    if (size == 0) {
        size++;
        ptrarr = new Geometrical_figure * [size];
        ptrarr[0] = figure;
    }
    else {
        size++;
        Geometrical_figure** temp;
        temp = ptrarr;
        ptrarr = new Geometrical_figure * [size];
        for (size_t i = 0; i < size; i++) {
            ptrarr[i] = temp[i];
        }
        ptrarr[size - 1] = figure;
    }

}
void Arrayptr::print() {
    for (size_t i = 0; i < size; i++) {
        std::cout << "-------------" << std::endl;
        ptrarr[i]->Show();
    }
}
Geometrical_figure* Arrayptr::operator[](int index) {
    return(ptrarr[index]);
}