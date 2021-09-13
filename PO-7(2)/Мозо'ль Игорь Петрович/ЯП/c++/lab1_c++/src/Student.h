//
// Created by Igor Mozol on 13.09.2021.
//
#ifndef STUDENT_H
#define STUDENT_H
#pragma once
#include <iostream>
#include <string>
using namespace std;
class Student{
    string name;
    int course;
    bool gender;
public:
    Student();
    Student(string stud_name,int stud_course,bool stud_gender);
    Student(const Student&stud);
    ~Student();
    string check_gender();
    string getName();
    int getCourse();
    bool getGender();
    void show();
    void setName(string stud_name);
    void setCourse(int stud_course);
    void setGender(bool stud_gender);
    void setData(string stud_name,int stud_course,bool stud_gender);
};
#endif //LABA_1_YAP_C___STUDENT_H
