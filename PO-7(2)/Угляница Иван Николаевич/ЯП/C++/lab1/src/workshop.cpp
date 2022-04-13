#include "workshop.h"
workshop::workshop()://конструктор по умолччанию
        name("Workshop"), chief("Ivan"),number(15)
{
    cout<<"Parameterless constructor worked"<<' '<<name<<' '<<chief<<' '<<number<<endl;
}
workshop::workshop (string n_name,string c_chief,int n_number)://конструктор с параметрами
name(n_name),chief(c_chief),number(n_number)
{
    cout<<"Constructor with parameters worked:"<<' '<<name<<' '<<chief<<' '<<number<<endl;
}

workshop::workshop(const workshop &copy_workshop):
        name(copy_workshop.name), chief(copy_workshop.chief), number(copy_workshop.number)
{
    cout<<"Copy constructor worked:"<<' '<<name<<' '<<chief<<' '<<number<<endl;
}

workshop::~workshop(){
    cout<<"Destructor worked:"<<' '<<name<<' '<<chief<<' '<<number<<endl;
}

void workshop::Show(){
    cout<<name<<' '<<chief<<' '<<number<<endl;
}
void workshop::setName(string new_name){
    name=new_name;
}
void workshop::setChief(string new_chief) {
    chief = new_chief;
}
void workshop::setNumber(int new_number){
    number=new_number;
}
string workshop::getName(){
    return name;
}
string workshop::getChief(){
    return chief;
}
int workshop::getNumber(){
    return number;
}

