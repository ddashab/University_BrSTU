//
// Created by sorryladies on 17.09.2021.
//

#include "Products.h"

void Product::Show()
{
    for (const Product* object : objects)
    {
        std::cout << object;
        std::cout <<" is " << object->mName << std::endl;
    }
}

Product :: ~Product()
{
    Product::objects.remove(this);
}


Product :: Product(const std::string& name, const double price) : mName(name), mPrice(price)
{
    objects.push_back(this);
}


void Product :: SetPrice(double price)
{
    mPrice = price;
}


const double Product :: GetPrice()
{
    return mPrice;
}


const std::string& Product :: GetName()
{
    return mName;
}


void Product :: SetName(const std::string& name)
{
    mName = name;
}


FoodProduct :: FoodProduct(const std::string& name, const double price) : Product(name, price)
{

}


void FoodProduct :: PrintCategory()
{
    std::cout << "This is FoodProduct" << std::endl;
}


MilkProduct :: MilkProduct(const std::string& name, const double price) : FoodProduct(name, price)
{

}


void MilkProduct :: PrintCategory()
{
    std::cout << "This is MilkProduct" << std::endl;
}


Toy :: Toy(const std::string& name, const double price) : Product(name, price)
{

}


void Toy :: PrintCategory()
{
    std :: cout << "This is Toy." << std::endl;
}