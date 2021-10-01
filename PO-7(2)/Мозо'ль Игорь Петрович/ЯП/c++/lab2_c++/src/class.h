#ifndef LABA_2_YAP_C___CLASS_H
#define LABA_2_YAP_C___CLASS_H
#include <iostream>
#include <string>
#include <list>
class Person{
protected:
    static std::list <Person*> obj_list;
    std::string name;
    int age;
public:
    Person(std::string Name, int Age);
    void add();
    virtual ~Person();
    int getAge();
    std::string getName();
    void setName(std::string name);
    void setAge(int age);
    virtual void show()=0;
    static void print();
};
class Teacher: public Person {
protected:
    int work_exp;
public:
    Teacher(std::string Name, int Age, int Work_exp);
    virtual ~Teacher();
    void show() override;
};
class Head_dep:public Teacher{
protected:
    std::string dep_name;
public:
    Head_dep(std::string Name, int Age, int Work_exp, std::string Dep_name);
    virtual ~Head_dep();
    void show() override;
};
class Student:public Person{
protected:
    int course;
public:
    Student(std::string Name, int Age, int Course);
    virtual ~Student();
    void show() override;
};

#endif //LABA_2_YAP_C___CLASS_H
