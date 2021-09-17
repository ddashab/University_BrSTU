//
// Created by sorryladies on 13.09.2021.
//
#ifndef RECEIPT_H
#define RECEIPT_H


#include <iostream>


class Receipt
{
    int number, data;
    float sum;
public:
    Receipt();
    Receipt(int nmb, int dt, float sm);
    Receipt(const Receipt& receipt);
    ~Receipt();

    int GetNumber(){return number;}
    int GetData(){return data;}
    float GetSum(){return sum;}
    void SetNumber(int newNumber){number = newNumber;}
    void SetData(int newData){data = newData;}
    void SetSum(float newSum){sum = newSum;}
    void Print(Receipt receipt);
};


#endif RECEIPT_H
