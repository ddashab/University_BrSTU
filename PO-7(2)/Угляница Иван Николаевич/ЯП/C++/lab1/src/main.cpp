#include "workshop.h"
int main() {
    setlocale(LC_ALL,"ru");
    workshop w;//Parameterless constructor
    workshop w1("Number_2","Abdul",124);//Constructor with parameters
    workshop w2(w1);//Copy constructor

    w.Show();
    w1.Show();
    w2.Show();
    w.setName("Number_1");
    cout<<w.getName()<<endl;
    w1.setChief("Alexandr");
    cout<<w1.getChief()<<endl;
    w2.setNumber(0);
    cout<<w2.getNumber()<<endl;
//task5
    void(workshop::*funcPtr)()=&workshop::Show;
    cout<<"Function pointer"<<endl;
    (w2.*funcPtr)();

//task6
    workshop*w3=new workshop;
    w3->Show();

}
