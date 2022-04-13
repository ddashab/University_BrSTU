#include "engine.h"

list <Engine*> Engine::objects{};

int main() {
    Combustion_engine first(1, 2, 3 );
    Diesel second(3, 2, 1, "stop");
    Combustion_engine third(7, 9, 4 );
    Turbojet_engine forth(6, 15, "Tesla");
    Engine::print();
}
