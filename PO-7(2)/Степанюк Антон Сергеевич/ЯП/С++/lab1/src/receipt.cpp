//
// Created by sorryladies on 13.09.2021.
//


#include"receipt.h"


Receipt::Receipt() : number(0), data(0), sum(0)
{
    std::cout << "The parameterless constructor is called for the object " << this << std::endl;
}


Receipt::Receipt(int nmb, int dt, float sm)
{
    std::cout << "The constructor with parameters is called for the object " << this << std::endl;
    number = nmb;
    data = dt;
    sum = sm;
}


Receipt::Receipt(const Receipt& receipt) : number(receipt.number), data(receipt.data), sum(receipt.sum)
{
    std::cout << "The copy constructor is called for the object " << this << std::endl;
}


Receipt::~Receipt()
{
    std::cout << "The destructor is called for the object " << this << std::endl;
}









