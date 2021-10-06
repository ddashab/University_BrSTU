#include "Figures.h"
#include "Ellipse.h"
#include "Box.h"
#include "Trapeze.h"
#include "ArrayFigures.h"

void checkBool (bool value){
    ///For nice output: True or False
    if (value == 0)
        cout << "False" << endl;
    if (value == 1)
        cout << "True" << endl;
}

int main(){
    setlocale(LC_ALL, "Russian");

    cout << "Написать программу, в которой описана иерархия классов: геометрические фигуры (эллипс, квадрат, трапеция).\n"
            "Описать класс для хранения коллекции фигур (массива указателей на базовый класс), в котором перегрузить \n"
            "операцию [], а также реализовать функцию подсчёта общей площади и периметра. Для базового класса и его \n"
            "потомков перегрузить операции ==, !=, =. Продемонстрировать работу операторов.\n" << endl;

    //checking overloaded operators for class Ellipse objects
    cout << "\n==================\n" << "Class Ellipse" << "\n==================\n" << endl;
    Ellipse ellipse1 = Ellipse(ellipse1.Read_a(), ellipse1.Read_b());
    ellipse1.showSquare();
    Ellipse ellipse2 = Ellipse(ellipse2.Read_a(), ellipse2.Read_b());
    ellipse2.showSquare();
    double check_value1 = 6.28318;
    double check_value2 = 11;
    bool check_ell = ellipse1.get_square() == check_value1;
    bool check2_ell = ellipse1.get_square() != check_value2;
    cout << ellipse1.get_square() << " == " << check_value1 << " : ";
    checkBool(check_ell);
    cout << ellipse1.get_square() << " != " << check_value2 << " : ";
    checkBool(check2_ell);
    cout << "Operator = " << endl;
    ellipse1.operator=(ellipse2);
    ellipse1.showSquare();

    //checking overloaded operators for class Box objects
    cout << "\n==================\n" << "Class Box" << "\n==================\n" << endl;
    Box box1 = Box(box1.Read_a());
    box1.showSquare();
    double check_value3 = 25;
    bool check_box = box1.get_square() == check_value3;
    cout << box1.get_square() << " == " << check_value3 << " : ";
    checkBool(check_box);

    //checking overloaded operators for class trapeze objects
    cout << "\n==================\n" << "Class Trapeze" << "\n==================\n" << endl;
    Trapeze trap1 = Trapeze(trap1.Read_a(), trap1.Read_b(), trap1.Read_c(), trap1.Read_d(), trap1.Read_h());
    trap1.showSquare();
    trap1.showPerimeter();
    double check_value4 = 12;
    double check_value5 = 4;
    bool check_trap = trap1.get_square() != check_value4;
    bool check_trap_per = trap1.get_perimeter() == check_value5;
    cout << trap1.get_square() << " != " << check_value4 << " : ";
    checkBool(check_trap);
    cout << trap1.get_perimeter() << " == " << check_value5 << " : ";
    checkBool(check_trap_per);

    //testing array of different classes objects
    cout << "\n==================\n" << "Testing Array" << "\n==================\n" << endl;
    Ellipse ellipse = Ellipse(1, 2);
    Box box = Box(5);
    Trapeze trap = Trapeze(2, 5, 11, 6, 4);

    ArrayFigures array(3);
    Figures *pEllipse = &ellipse;
    Figures *pBox = &box;
    Figures *pTrapeze = &trap;
    array[0] = pEllipse;
    array[1] = pBox;
    array.insertBefore(pTrapeze, 1);  //array[1]
    array.remove(1);

    for (int i = 0; i < 3; i++) {
        array[i]->showSquare();
        array[i]->showPerimeter();
    }
    array.erase();

    return 0;
}