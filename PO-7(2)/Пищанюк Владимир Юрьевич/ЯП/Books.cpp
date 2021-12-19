#include <iostream>
#include "Books.h"
using namespace std;


PrintItem::PrintItem(const char* name, float price, bool isAdd) :
    name(name), price(price) {
    if (isAdd) Add();
    cout << "Created PrintItem \"" << name << "\"\n";
}
PrintItem::~PrintItem() { cout << "Deleted PrintItem \"" << name << "\"\n"; }
void PrintItem::Add() {
    PrintItem** temp = items;
    items = new PrintItem * [count + 1];
    for (int i = 0; i < count; i++) items[i] = temp[i];
    items[count] = this; count++;
}
void PrintItem::listItems() {
    for (int i = 0; i < count; i++) items[i]->Print();
    cout << endl;
}

Magazine::Magazine(const char* name, float price, const char* publisher) : PrintItem(name, price, false), publisher(publisher) { cout << "Magazine was created \"" << name << "\"\n"; }
Magazine::~Magazine() { cout << "Magazine was deleted \"" << name << "\"\n"; }
void Magazine::Print() { cout << "Magazine: \"" << name << "\", with price: " << price << ", author: " << publisher << "\n"; }

Book::Book(const char* name, float price, const char* author) : PrintItem(name, price, true), author(author) { cout << "Book was created \"" << name << "\"\n"; }
Book::~Book() { cout << "Book was deleted \"" << name << "\"\n"; }
void Book::Print() { cout << "Book\"" << name << "\", price: " << price << ", author: " << author << "\n"; }

TextBook::TextBook(const char* name, float price, const char* author, int grade) : Book(name, price, author), grade(grade) { cout << "Textbook was created \"" << name << "\"\n"; }
TextBook::~TextBook() { cout << "Textbook was deleted\"" << name << "\"\n"; }
void TextBook::Print() { cout << "TextBook: \"" << name << "\", price: " << price << ", author: " << author << ", grade: " << grade << "\n"; }
