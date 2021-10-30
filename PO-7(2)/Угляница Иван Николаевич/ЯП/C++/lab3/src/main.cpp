#include "header.h"
int main() {
    Tetrahedron a(2);
    Cube b(2);
    Cylinder c(7,8);
    bool check1 = a==b;
    bool check2 = a!=c;
    std::cout<<check1<<std::endl;
    std::cout<<check2<<std::endl;
    Arrayptr ptr;
    ptr.add(&a);
    ptr.add(&b);
    ptr.add(&c);
    ptr.print();
    *ptr[0]=*ptr[1];
    std::cout<<std::endl<<"After ="<<std::endl;
    ptr.print();
}
