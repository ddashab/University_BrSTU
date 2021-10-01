#include "class.h"

Person :: Person(std::string Name, int Age):
name(Name),age(Age)
{
    std::cout <<"Person construct\n";
    add();
}
void Person :: add(){
    obj_list.push_back(this);
}
Person :: ~Person(){
    std::cout << "Person desruct\n";
}
int Person:: getAge() {
    return age;
}
std::string Person:: getName(){
    return name;
}

void Person:: setName(std::string name) {
    Person::name = name;
}

void Person:: setAge(int age) {
    Person::age = age;
}

void Person:: print(){
    if(!obj_list.empty()) {
        int i = 1;
        for (Person *obj: obj_list) {
            std::cout << i << "-st object:\n";
            obj->show();
            i++;
        }
    }
}


Teacher:: Teacher(std::string Name, int Age, int Work_exp):
Person(Name,Age), work_exp(Work_exp){
        std::cout <<"Teacher construct\n";
}

Teacher:: ~Teacher(){
    std::cout <<"Teacher destruct\n";
}

void Teacher:: show() {
std::cout <<"Teacher name - "<< name <<"\n";
std::cout <<"Age - " << age <<" years\n";
std::cout <<"Work experience - "<<work_exp <<" years\n";
}


Head_dep:: Head_dep(std::string Name, int Age, int Work_exp, std::string Dep_name):
Teacher(Name,Age,Work_exp),dep_name(Dep_name){
        std::cout <<"Head_dep construct\n";
}
Head_dep:: ~Head_dep(){
    std::cout <<"Head_dep destruct\n";
}
void Head_dep:: show() {
std::cout <<"Name - "<< name <<"\n";
std::cout <<"Age - " << age <<" years\n";
std::cout <<"Work experience - "<<work_exp <<" years\n";
std::cout <<"Department name - "<<dep_name <<"\n";
}


Student:: Student(std::string Name, int Age, int Course):
Person(Name,Age),course(Course){
        std::cout <<"Student construct\n";
}
Student:: ~Student(){
    std::cout <<"Student destruct\n";
}
void Student:: show()  {
std::cout <<"Student name - "<< name <<"\n";
std::cout <<"Age - " << age <<" years\n";
std::cout <<"Course number - "<<course <<"\n";
}