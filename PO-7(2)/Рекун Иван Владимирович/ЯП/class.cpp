#include "class.h"

Printed_edition::Printed_edition(std::string Name, int Date_foundation) :
    name(Name), date_foundation(Date_foundation)
{
    std::cout << "Printed_edition construct\n";
    add();
}
void Printed_edition::add() {
    obj_list.push_back(this);
}
Printed_edition :: ~Printed_edition() {
    std::cout << "Printed_edition desruct\n";
}
int Printed_edition::getDate_foundation() {
    return date_foundation;
}
std::string Printed_edition::getName() {
    return name;
}

void Printed_edition::setName(std::string name) {
    Printed_edition::name = name;
}

void Printed_edition::setDate_foundation(int date_foundation) {
    Printed_edition::date_foundation = date_foundation;
}

void Printed_edition::print() {
    if (!obj_list.empty()) {
        int i = 1;
        for (Printed_edition* obj : obj_list) {
            std::cout << i << "-st object:\n";
            obj->show();
            i++;
        }
    }
}


Journal::Journal(std::string Name, int Date_foundation, int Price) :
    Printed_edition(Name, Date_foundation), price(Price) {
    std::cout << "Journal construct\n";
}

Journal:: ~Journal() {
    std::cout << "Journal destruct\n";
}

void Journal::show() {
    std::cout << "Journal name - " << name << "\n";
    std::cout << "Date of foundation - " << date_foundation << " years\n";
    std::cout << "Journal price - " << price << " euro\n";
}


Textbook::Textbook(std::string Name, int Date_foundation, int Price, std::string Lesson_name) :
    Journal(Name, Date_foundation, Price), lesson_name(Lesson_name) {
    std::cout << "Textbook construct\n";
}
Textbook:: ~Textbook() {
    std::cout << "Textbook destruct\n";
}
void Textbook::show() {
    std::cout << "Name - " << name << "\n";
    std::cout << "Date of writing - " << date_foundation << " years\n";
    std::cout << "Price - " << price << " euro\n";
    std::cout << "Lesson name - " << lesson_name << "\n";
}


Book::Book(std::string Name, int Date_foundation, std::string Author):
    Printed_edition(Name, Date_foundation), author(Author) {
    std::cout << "Book construct\n";
}
Book:: ~Book() {
    std::cout << "Book destruct\n";
}
void Book::show() {
    std::cout << "Book name - " << name << "\n";
    std::cout << "Date of writing - " << date_foundation << " years\n";
    std::cout << "Author - " << author << "\n";
}