//
// Created by ASUS on 15.10.2021.
//
//12) двигатель, двигатель внутреннего сгорания, дизель, турборе-
//активный двигатель;

#ifndef LAB_2_ENGINE_H
#define LAB_2_ENGINE_H
#include "iostream"
#include "string"
#include "list"
using namespace std;


class Engine{//двигатель
    static list<Engine*>objects;
protected:
    int power_r;//цена
    float cost_t;//стоимость
public:
    Engine(int power, float cost);
    virtual ~Engine();
    static void print();
    virtual void show() = 0;
    void add();
};


class Combustion_engine : public Engine{//двигатель внутреннего сгорания
protected:
    int fuel_l;//расход топлива
public:
    Combustion_engine(int power, float cost, int fuelL);
    void show() override;
    virtual ~Combustion_engine();
};


class Diesel : public Combustion_engine{//дизель
protected:
    string transport_t;//вид транспотра
public:
    Diesel(int power, float cost, int fuel, string transport_t);
    virtual ~Diesel();
    void show() override;
};


class Turbojet_engine : public Engine{//турбореактивный двигатель
protected:
    string vendor_r; //поставщик
public:
    Turbojet_engine(int power, float cost, string vendor);
    virtual ~Turbojet_engine();
    void show() override;
};
#endif //LAB_2_ENGINE_H


//1. Для определения иерархии классов связать отношением наследо-
//вания классы, приведенные в приложении (для заданного варианта).
//Из перечисленных классов выбрать один, который будет стоять во
//главе иерархии. Это абстрактный класс.
//2. Определить в классах все необходимые конструкторы и деструк-
//тор.
//
//3. Компонентные данные класса специфицировать как protected.
//4. Пример определения статических компонентов:
//static person* begin; // указатель на начало списка
//static void print(void); // просмотр списка
//5. Статическую компоненту-данное инициализировать вне определе-
//ния класса, в глобальной области.
//6. Для добавления объекта в список предусмотреть метод класса,
//т.е. объект сам добавляет себя в список. Например, a.Add() −
//объект a добавляет себя в список.
//Включение объекта в список можно выполнять при создании объек-
//та, т.е. поместить операторы включения в конструктор. В случае
//иерархии классов, включение объекта в список должен выполнять
//только конструктор базового класса. Вы должны продемонстрировать
//оба этих способа.
//7. Список просматривать путем вызова виртуального метода Show
//каждого объекта.
//8. Статический метод просмотра списка вызывать не через объект, а
//через класс.
//9. Определение классов, их реализацию, демонстрационную про-
//грамму поместить в отдельные файлы.