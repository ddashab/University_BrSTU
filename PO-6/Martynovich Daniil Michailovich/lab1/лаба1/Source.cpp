#include <iostream>
#include <windows.h>
#include <string.h>
#include <tchar.h>
#include <ctime>
#include <string>
#define _CRT_SECURE_NO_WARNINGS
void MoveASM(char* str, size_t cnt)
{
    size_t len = strnlen_s(str, 32) - 1;
    __asm
    {
        push eax
        push ecx
        push ebx                          
        mov ecx, cnt
        lbl1 :
        push ecx
            xor eax, eax
            mov ebx, str
            mov al, byte ptr[ebx]
            push eax
            mov ecx, len
            mov esi, str
            inc esi
            mov edi, str
            rep movsb
            pop eax
            mov ebx, str
            add ebx, len
            mov byte ptr[ebx], al
            pop ecx
            dec ecx
            jecxz ext
            jmp lbl1
            ext :
            pop ebx
            pop ecx
            pop eax
    }
}
void MOVEonC(char* str)
{
    int count = strlen(str)-1;

       for(int i = 0; i < count; i++) 
       {               
           std::swap(str[count], str[i]);
       }
     
}
int _tmain(int argc, _TCHAR* argv[])
{
    setlocale(LC_ALL, "ru");
 
    char* str = new char[32];
    char* str1 = new char[32];
    int count = strlen(str) - 1;
    std::cout << "Input strok:\n";
    std::cin >> str;
    strcpy(str1, str);

    srand(time(0));
    std::cout << "\nAssembler code\n";
    MoveASM(str, count);
    std::cout << "\nResult:\n" << str;
    std::cout << "\nTime ASM: " << clock() / 1000.0;
    std::cout << "\n";

    srand(time(0));
    std::cout << "\nC++ code\n";
    MOVEonC(str1);
    std::cout << "\nResult:\n"<<str1;
    std::cout << "\nTime C++: " << clock() / 1000.0;
    std::cout << "\n";
    std::cin.get();

    system("pause");
    return 0;
}

