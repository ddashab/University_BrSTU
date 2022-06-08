#include<iostream>
#include<string>
#include<chrono>

#pragma warning(disable : 4996)

using namespace std;

void reverse_str(char* str, int length);
void reverse_str_asm(char* str, int lenght);

int main(int argc, char* argv[])
{
	string str;
	cout << "String: ";
	getline(cin, str);
	reverse_str(strdup(str.c_str()), str.length());
	reverse_str_asm(strdup(str.c_str()), str.length());
	return 0;
}

void reverse_str(char* str, int lenght)
{
	auto start = chrono::high_resolution_clock::now();
	int last_character_index = lenght - 1;
	for (int i = 0; i < lenght / 2; i++)
	{
		swap(str[i], str[last_character_index - i]);
	}
	auto end = chrono::high_resolution_clock::now();
	chrono::duration<float> duration = end - start;
	cout << "Result (C++): " << str << endl;
	cout << "Time: " << duration.count() << endl;
}


void reverse_str_asm(char* str, int lenght)
{
	auto start = chrono::high_resolution_clock::now();
    __asm {
		mov ecx, lenght
		mov eax, str
		mov esi, eax
		add eax, ecx
		mov edi, eax
		dec edi
		shr ecx, 1

		reverse_loop:
			mov al, [esi]
			mov bl, [edi]
			mov [esi], bl
			mov [edi], al
			inc esi
			dec edi
			dec ecx
			jnz reverse_loop
    };
	auto end = chrono::high_resolution_clock::now();
	chrono::duration<float> duration = end - start;
	cout << "Result (asm): " << str << endl;
	cout << "Time: " << duration.count() << endl;
}
