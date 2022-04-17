#include <iostream>
#include <string>
#include <sstream>
 
std::string inputString()
{
    std::string result;
    std::getline(std::cin, result);
    return result;
}
 
std::string reverseWords(const std::string& instr)
{
    std::string result, token;
    std::istringstream iss(instr);
 
    while (std::getline(iss, token, ' '))
    {
        if (token.length())
        {
            result = !result.length() ? token : (token + ' ') + result;
        }
        
    }
    return result;
}
 
int main()
{
    std::cout << reverseWords(inputString()) << std::endl;
    system("pause");
    return 0;
}