#include <iomanip>
#include "Books.h"

int PrintItem::count = 0; PrintItem** PrintItem::items = nullptr;

int main() {
    setlocale(LC_ALL, "Russian");
    Magazine Dig_mag("Reader's Digest", 5.99, "Trusted Media Brands");
    Dig_mag.Add(); 
    Book CnP("Harry Potter and the Philosopher's Stone", 9.99, "Joanne Rowling"); 
    Book FnC("Alice’s Adventures in Wonderland", 9.99, "Lewis Carroll"); 
    TextBook Math1("Math", 5.99, "Ministry of education of the Republic of Belarus", 1); 

    PrintItem::listItems();
}
