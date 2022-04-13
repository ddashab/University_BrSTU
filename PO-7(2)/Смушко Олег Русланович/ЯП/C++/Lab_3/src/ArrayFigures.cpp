//
// Created by Олег on 04.10.2021.
//

#include "ArrayFigures.h"
ArrayFigures::ArrayFigures() {  //constructor without parameters
    m_length = 0;
    m_data = nullptr;
}

ArrayFigures::ArrayFigures(int length) {  //constructor with parameters
    m_length = length;
    assert(length >= 0);
    if (length > 0)
        m_data = new ptr[length];
    else
        m_data = nullptr;
}

ArrayFigures::~ArrayFigures() {  //destructor
    delete[] m_data;
}

void ArrayFigures::erase() {  //function to return the class to its original state
    delete[] m_data;
    m_data = nullptr;
    m_length = 0;
}

void ArrayFigures::insertBefore(ptr value, int index) {
    assert(index >= 0 && index <= m_length);  //checking index
    ptr *data = new ptr[m_length+1];  //creating new array
    for (int before = 0; before < index; ++before)  //copying all elements before index
        data[before] = m_data[before];
    data[index] = value;  //inserting our new element
    for (int after = index; after < m_length; ++after)  //copying all elements after inserted element
        data[after+1] = m_data[after];
    delete[] m_data;
    m_data = data;
    ++m_length;
}

void ArrayFigures::remove(int index) {
    assert(index >= 0 && index < m_length);  //checking index
    if (m_length == 1){  //if it's the last element of array
        erase();
        return;
    }
    ptr *data = new ptr[m_length-1];  //creating new array
    for (int before = 0; before < index; ++before)  //copying all elements before index
        data[before] = m_data[before];
    for (int after = index+1; after < m_length; ++after)  //copying all elements after deleted element
        data[after-1] = m_data[after];
    delete[] m_data;
    m_data = data;
    --m_length;
}