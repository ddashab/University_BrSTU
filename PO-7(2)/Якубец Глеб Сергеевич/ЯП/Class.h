#pragma once
#include <string>
#include <iostream>
using namespace std;
class State {
	string name;
	string form;
	float area;
public:
	State();
	State(string, string, float);
	State(const State&);
	~State();
	void set_name(string);
	void set_form(string);
	void set_area(float);
	void read();
	void show();
};