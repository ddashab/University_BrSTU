//
// Created by Олег on 04.10.2021.
//

#ifndef LAB_3_ARRAYFIGURES_H
#define LAB_3_ARRAYFIGURES_H
#include "Figures.h"
#include <cassert>
typedef Figures *ptr;
class ArrayFigures{  //collection of objects class
private:
    int m_length;
    ptr *m_data;
public:
    ArrayFigures();
    ArrayFigures(int length);
    ~ArrayFigures();
    void erase();
    void insertBefore(ptr value, int index);
    void remove(int index);
    ptr &operator[] (int index){  //overloading [] operator
        assert(index >= 0 && index < m_length);
        return m_data[index];
    }
};
#endif //LAB_3_ARRAYFIGURES_H
