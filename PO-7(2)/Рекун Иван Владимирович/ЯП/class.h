#ifndef LABA_2_YAP_C___CLASS_H
#define LABA_2_YAP_C___CLASS_H
#include <iostream>
#include <string>
#include <list>
class Printed_edition {
protected:
    static std::list <Printed_edition*> obj_list;
    std::string name;
    int date_foundation;
public:
    Printed_edition(std::string Name, int Date_foundation);
    void add();
    virtual ~Printed_edition();
    int getDate_foundation();
    std::string getName();
    void setName(std::string name);
    void setDate_foundation(int date_foundation);
    virtual void show() = 0;
    static void print();
};
class Journal : public Printed_edition {
protected:
    int price;
public:
    Journal(std::string Name, int Date_foundation, int Price);
    virtual ~Journal();
    void show() override;
};
class Textbook :public Journal {
protected:
    std::string lesson_name;
public:
    Textbook(std::string Name, int Date_foundation, int Price, std::string Lesson_name);
    virtual ~Textbook();
    void show() override;
};
class Book :public Printed_edition {
protected:
    std::string author;
public:
    Book(std::string Name, int Date_foundation, std::string author);
    virtual ~Book();
    void show() override;
};

#endif //LABA_2_YAP_C___CLASS_H