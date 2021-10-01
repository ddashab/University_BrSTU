#include "place.h"
#include "region.h"
#include "town.h"
#include "megapolis.h"

int main(){
    list<Place*> places;  //making list with class type

    auto *brestRegion = new Region("Brest", 25);
    brestRegion->set_count(58);  //testing function set_count()
    //adding elements to the list
    places.push_back(brestRegion);

    places.push_back(new Region("Minsk", 125));

    places.push_back(new Town("Mogilev", 439.11));
    places.push_back(new Town("Gomel", 281.70));

    auto *vitebskRegion = new Megapolis("Vitebsk", 391.42, 210000);

    places.push_back(new Megapolis("Grodno", 171.95, 326800));
    places.push_back(vitebskRegion);

    //display all elements of the list
    std::for_each(places.begin(), places.end(), [](Place* place){
        place->show();
    });

    cout << "Testing get_population() : " << vitebskRegion->get_population() << endl;

    return 0;
}