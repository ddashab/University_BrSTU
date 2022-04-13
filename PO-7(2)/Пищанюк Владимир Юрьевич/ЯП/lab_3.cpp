#include "exam.h"


int main() {
    setlocale(LC_ALL, "russian");
    cout << "Creating class objects in different ways:" << endl;
    auto* exam_noParam = new Exam;  
    auto* exam_param = new Exam("Vova", 4, 1); 
    auto* exam_copy = new Exam(*exam_param);  

    cout << "\n\nAccessing Objects Through Field Modification Methods: " << endl;
    cout << "\nChange name: ";
    exam_noParam->SetName("first object");
    exam_noParam->Print();

    cout << "\nChange data: ";
    exam_param->SetDate(5);
    exam_param->Print();

    cout << "\nUsing a pointer to an object of a class: " << endl;
    Exam* exam_ptr; 
    exam_ptr = &*exam_copy;
    cout << "\nObject, before changing it through a pointer: ";
    exam_copy->Print();
    cout << "\nModifying an object via a pointer: ";
    exam_ptr->SetName("Gleb");
    cout << "\nOutputting an object through a pointer: ";
    exam_ptr->Print();
    cout << "\nOutput of the object itself: ";
    exam_copy->Print();


    cout << "\nUsing a pointer to a class method: " << endl;
    cout << "\nUsing a pointer to a class method: ";
    void (Exam:: * PrintP)() const;
    cout << "\nAssigning a Method to a Pointer: ";
    PrintP = &Exam::Print;
    cout << "\nOutputting an object through a pointer: ";
    (exam_copy->*PrintP)();


    cout << "\n\nDel obj: \n";
    delete exam_noParam;
    delete exam_param;
    delete exam_copy;
}