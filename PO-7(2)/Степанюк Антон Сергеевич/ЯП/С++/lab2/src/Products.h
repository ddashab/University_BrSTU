//
// Created by sorryladies on 14.09.2021.
//

#ifndef YAPLAB2_PRODUCT_H
#define YAPLAB2_PRODUCT_H


#include <list>
#include <iostream>
#include <string>


class Product
{
protected:
    static std::list <Product*> objects;
    double mPrice;
    std::string mName;
public:
    Product(const std::string& name, const double price);
    void SetPrice(double price);
    void SetName(const std::string& name);
    const std::string& GetName();
    const double GetPrice();
    static void Show();
    virtual void PrintCategory() = 0;
    ~Product();
};


class FoodProduct : public Product
{
public:
    FoodProduct(const std::string& name, const double price);
    virtual void PrintCategory() override;
};


class MilkProduct : public FoodProduct
{
public:
    MilkProduct(const std::string& name, const double price);
    virtual void PrintCategory() override;
};


class Toy : public Product
{
public:
    Toy(const std::string& name, const double price);
    virtual void PrintCategory() override;
};

#endif YAPLAB2_PRODUCT_H
