#include "class.h"
std::list <Printed_edition*> Printed_edition::obj_list;

int main() {
    Journal first("Accept the lab, pls", 1945, 100);
    Textbook second("Programming Language", 2020, 30, "OAiP");
    Book third("Passing the session", 2021, "Gleb Yakubets");
    Textbook fourth("Math for down", 2016, 10, "Mathematic");
    Printed_edition::print();
}