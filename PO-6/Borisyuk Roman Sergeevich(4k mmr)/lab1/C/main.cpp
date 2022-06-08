#include <iostream>
#include <string>

using namespace std;

int main() {
    string str = "Hello world!";
    char last_char = str[str.length() - 1];

    for (int i = str.length(); i > 0; i--){
        str[i] = str[i - 1];
    }

    str[0] = last_char;
    cout << str;

}
