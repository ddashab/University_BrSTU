#include "Student.h"
int main(){
    Student first;
    Student second("Maria",4,0);
    Student third(first);

    void(Student::*ShowShow)()=&Student::show;
    (first.*ShowShow)();

    Student* fourth=new Student;
    cout <<fourth->getName()<<'\n';
    fourth->setData("Tolik",5,1);
    fourth->show();
}
