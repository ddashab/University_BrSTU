//
// Created by Igor Mozol on 13.09.2021.
//
#include "Student.h"
Student::Student():
        name("Ahmed"),course(1),gender(1)
{
    cout<<"Constructor with no parametres worked for \n"<<
        name<<"  "<<course<<" course " << check_gender()<<'\n';
}
Student::Student(string stud_name,int stud_course,bool stud_gender):
name(stud_name),course(stud_course),gender(stud_gender)
{
    cout<<"Constructor with parametres worked for \n"<<
        name<<"  "<<course<<" course " << check_gender()<<'\n';
}
Student::Student(const Student&stud):
        name(stud.name),course(stud.course),gender(stud.gender)
{

    cout<<"Constructor copy worked for\n"<<
        name<<"  "<<course<<" course " << check_gender()<<'\n';
}
Student::~Student(){
    cout<<"Destructor worked for\n"<<
        name<<"  "<<course<<" course " << check_gender()<<'\n';
}
string Student::check_gender(){
    if(gender==1){
        return "Man";
    }
    else return "Woman";
}
string Student::getName(){
    return name;
}
int Student::getCourse(){
    return course;
}
bool Student::getGender(){
    return gender;
}
void Student::show(){
    cout<<name<<"  "<<course<<" course " << check_gender()<<'\n';
}
void Student::setName(string stud_name){
    name=stud_name;
}
void Student::setCourse(int stud_course){
    course=stud_course;
}
void Student::setGender(bool stud_gender){
    gender=stud_gender;
}
void Student::setData(string stud_name,int stud_course,bool stud_gender){
    name=stud_name;
    course=stud_course;
    gender=stud_gender;
}

