//
// Created by Igor Mozol on 29.10.2021.
//

#ifndef LABA_3_YAP_C___FIGURES_H
#define LABA_3_YAP_C___FIGURES_H
#include <iostream>
#include <cmath>
class Sphere{
protected:
    double square;
    double volume;
    const double pi = 3.141592653589793;
    double radius;
public:
    Sphere(double radius_);
    virtual void print();
    virtual double calc_square();
    virtual double calc_volume();
    void setVolume(double volume_);
    bool operator ==(const Sphere& right);
    bool operator !=(const Sphere& right);
    Sphere operator =(const Sphere& right);

};
class Conus: public Sphere{
protected:
    double height;
    double generatrix;
public:
    Conus(double radius_,double height_, double generatrix_);
    void print();
    double calc_square();
    double calc_volume();
};

class Pyramid: public Conus{
public:
    Pyramid(double heigth_,double square_);
    void print();
    double calc_volume();
};
class Figures{
private:
    int length = 0;
    Sphere** list = new Sphere*[length];
public:
    void add(Sphere* added);
    Sphere* operator [](int num);
    int getlength();
};

#endif //LABA_3_YAP_C___FIGURES_H
