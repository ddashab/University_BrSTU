//
// Created by Igor Mozol on 29.10.2021.
//
#include "figures.h"

    Sphere::Sphere(double radius_):
            radius(radius_)
    {
        volume = calc_volume();
        square = calc_square();

    }
    void Sphere:: print(){
        std::cout << "Square: " << square <<", Volume: " << volume<< ", Radius: " <<radius<< std::endl;
    }
   double Sphere:: calc_square(){
        return 4 * pi * pow(radius, 2);
    }
    double Sphere:: calc_volume(){
        return (double)4/3 * pi * pow(radius, 3);
    }
    void Sphere:: setVolume(double volume_){
        volume = volume_;
    }

    bool Sphere:: operator ==(const Sphere& right){
        return volume == right.volume;
    }
    bool Sphere:: operator !=(const Sphere& right){
        return !(volume ==right.volume);
    }

    Sphere Sphere:: operator =(const Sphere& right){
        volume = right.volume;
        return *this;
    }

    Conus:: Conus(double radius_,double height_, double generatrix_):
            Sphere(radius_),height(height_), generatrix(generatrix_)
    {
        volume = calc_volume();
        square = calc_square();
    }
    void Conus:: print(){
        std::cout << "Square: " << square <<", Volume: " << volume<< ", Radius: " <<radius;
        std::cout << " Height: " <<height<<", Generatrix: " << generatrix <<std::endl;
    }
    double Conus:: calc_square(){
        return pi * radius * (radius + generatrix);
    }
    double Conus:: calc_volume(){
        return (double)1/3 * pi * pow(radius, 2) * height;
    }


    Pyramid::Pyramid(double heigth_,double square_):
            Conus(0, heigth_, 0)
    {
        square = square_;
        volume = calc_volume();
    }
    void Pyramid::print(){
        std::cout << "Square: " << square <<", Volume: " << volume<< " Height: " <<height<<std::endl;
    }

    double Pyramid::calc_volume(){
        return (double)1/3 * square * height;
    }


    void Figures:: add(Sphere* added){
        Sphere** new_list = new Sphere*[++length];
        for(int i = 0; i< length - 1; i++){
            new_list[i] = list[i];
        }
        new_list[length-1] = added;
        list = new_list;
    }
    Sphere* Figures:: operator [](int num){
    if(num >=0 or num <=length){
        return list[num];
    }


}
int Figures::getlength() {
    return length;
}




