//
// Created by lenovo on 16.09.2021.
//
#ifndef LAB_2_HEADER_H
#define LAB_2_HEADER_H
#include <iostream>
#include <list>
using namespace std;
class receipt{
protected:
    string bank;
    static  list <receipt*> my_list;
public:
    receipt(string n_bank);
    static void show_list();
    virtual void print()= 0;
    void add();
    virtual ~receipt();
};
//накладная
class invoice: public receipt{
protected:
    int payment_amount;
public:
    invoice(string n_bank,int n_payment_amount);
    virtual void print() override;
    virtual ~invoice();
};
//документ
class document: public receipt{
protected:
    string content;
public:
    document(string n_bank,string n_content);
    virtual void print() override;
    virtual ~document();
};

//бланк
class form: public receipt{
protected:
    string purpose;
public:
    form(string n_bank,string n_purpose);
    virtual void print() override;
    virtual ~form();
};

#endif //LAB_2_HEADER_H
