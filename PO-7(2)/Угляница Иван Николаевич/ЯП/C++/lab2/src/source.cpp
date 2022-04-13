#include "header.h"

void receipt::show_list() {
    list<receipt*> temp=my_list;
    for (size_t i = 0;i<my_list.size();i++){
        temp.front()->print();
        temp.pop_front();
    }

}
void receipt:: add(){
    my_list.push_back(this);
}
receipt::receipt(string n_bank):
    bank(n_bank){
    add();
}
receipt::~receipt(){

}

//

invoice::invoice(string n_bank, int n_payment_amount):
    receipt(n_bank),payment_amount(n_payment_amount){
}


void invoice::print() {
    cout<<"Invoice from bank " <<bank<<" payment amount "<<payment_amount<<endl;
}
invoice::~invoice() {
}

//

document::document(string n_bank, string n_content):
        receipt(n_bank),content(n_content){

}

void document::print() {
    cout<<"Document from bank "<<bank <<" with content " <<content<<endl;
}
document::~document() {
}

//

form::form(string n_bank, string n_purpose):
        receipt(n_bank),purpose(n_purpose)
{
}

void form::print() {
    cout<<"Blank from bank " <<bank<<" with "<<purpose<<endl;
}
form::~form() {
}
