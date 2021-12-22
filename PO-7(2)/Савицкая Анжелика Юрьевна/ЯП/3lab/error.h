#pragma once
#include <iostream>
class IndexError {
protected:
	char* message;
public:
	IndexError(const char* message);
	~IndexError();
	char* get_message();
};
