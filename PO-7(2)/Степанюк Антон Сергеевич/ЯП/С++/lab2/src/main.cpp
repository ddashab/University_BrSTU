#include "Products.h"

std::list <Product*> Product::objects{};

int main() {
    FoodProduct chocolate{"Milka", 2};
    Toy gachiStick{"For Big Boys", 300};
    MilkProduct milk{"ToPmIlK", 1.05};
    Product :: Show();
}
