#include "class.h"
std::list <Person*> Person:: obj_list;

int main() {
    Teacher first("Irina",45,10);
    Head_dep second("Anna",56,30,"IIT");
    Student third("Ivan",20,3);
    Head_dep fourth("Dmitriy",33,10,"FL");
    Person::print();
}
