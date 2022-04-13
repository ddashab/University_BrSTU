#include <iostream>
#include "header.h"
using namespace std;
list <receipt*> receipt::my_list{};
int main() {
    document b("big dick club","some dicks");
    form a("Belarusbank","learn about salary");
    invoice g ("Trust",34);
    a.add();
    receipt::show_list();


}