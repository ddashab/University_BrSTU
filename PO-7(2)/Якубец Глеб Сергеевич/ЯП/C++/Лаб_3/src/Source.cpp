#include <iostream>;
#include <cmath>

using namespace std;


class Triangle {
	int s1;
	int s2;
	int s3;
public:
	virtual double Area() = 0;
	virtual int Perim() = 0;
};

class Equilateral : public Triangle {
	int sideline;
public:
	Equilateral(int sd);
	double Area();
	int Perim();
	bool operator== (const Equilateral& other) {
		return (sideline == other.sideline);
	}
	bool operator!= (const Equilateral& other) {
		return !(*this == other);
	}
	Equilateral& operator= (const Equilateral& other) {
		sideline = other.sideline;
		return *this;
	}
};

class Isosceles : public Triangle {
	int sideline;
	int baseline;
public:
	Isosceles(int sd, int bs);
	double Area();
	int Perim();
	bool operator== (const Isosceles& other) {
		return (sideline == other.sideline) && (baseline == other.baseline);
	}
	bool operator!= (const Isosceles& other) {
		return !(*this == other);
	}
	Isosceles& operator= (const Isosceles& other) {
		sideline = other.sideline;
		baseline = other.baseline;
		return *this;
	}
};

class Rectangular : public Triangle {
	int hypoten;
	int catet1;
	int catet2;
public:
	Rectangular(int hp, int c1, int c2);
	double Area();
	int Perim();
	bool operator== (const Rectangular& other) {
		return (catet2 == other.catet2) && (catet1 == other.catet1);
	}
	bool operator!= (const Rectangular& other) {
		return !(*this == other);
	}
	Rectangular& operator= (const Rectangular& other) {
		hypoten = other.hypoten;
		catet1 = other.catet1;
		catet2 = other.catet2;
		return *this;
	}
};

typedef Triangle* ptr;

class Collection {
	ptr* m_trgls;
	int m_count;
public:
	Collection(int trCount) {
		m_trgls = new ptr[trCount];
		for (int i = 0; i < trCount; i++) {
			m_trgls[i] = nullptr;
		}
		m_count = trCount;
	}
	~Collection() {
		for (int i = 0; i < m_count; i++) {
			if (m_trgls[i] != nullptr) delete m_trgls[i];
		}
		delete[] m_trgls;
	}
	double AllAreas() {
		double x = 0;
		for (int i = 0; i < m_count; i++) {
			x += m_trgls[i]->Area();
		}
		return(x);
	}
	int AllPerim() {
		int x = 0;
		for (int i = 0; i < m_count; i++) {
			x += m_trgls[i]->Perim();
		}
		return(x);
	}
	Triangle* operator[] (int index) const {
		if (index < 0 || index >= m_count) {
			cout << "Элемента с таким " << index << " индексом нет в массиве" << endl;
		}
		else {
			return m_trgls[index];
		}
	}
	Triangle*& operator[] (int index) {
		if (index < 0 || index >= m_count) {
			cout << "Элемента с таким " << index << " индексом нет в массиве" << endl;
		}
		else {
			return m_trgls[index];
		}
	}
};


Equilateral::Equilateral(int sd) {
	sideline = sd;
}
double Equilateral::Area() {
	int x = sideline;
	double height = sqrt(pow(x,2) - pow(x/2, 2));
	double sq = x * height;
	return(sq / 2);
}
int Equilateral::Perim() {
	return(3 * sideline);
}


Isosceles::Isosceles(int sd, int bs) {
	sideline = sd;
	baseline = bs;
}
double Isosceles::Area() {
	int x = sideline;
	int y = baseline;
	double height = sqrt(pow(x, 2) - pow((y/2), 2));
	double sq = y * height;
	return(sq / 2);
}
int Isosceles::Perim() {
	return(sideline * 2 + baseline);
}


Rectangular::Rectangular(int hp, int c1, int c2) {
	hypoten = hp;
	catet1 = c1;
	catet2 = c2;
}
double Rectangular::Area() {
	int x1 = catet1;
	int x2 = catet2;
	int x = x1 * x2;
	return(x / 2);
}
int Rectangular::Perim() {
	return(hypoten + catet1 + catet2);
}


int main() {
	setlocale(LC_ALL, "rus");
	Equilateral Triangle_1 = Equilateral(5);
	Isosceles Triangle_2 = Isosceles(10, 12);
	Rectangular Triangle_3 = Rectangular(10, 8, 6);
	cout << Triangle_1.Perim() << endl << Triangle_1.Area() << endl << Triangle_2.Perim() << endl << Triangle_2.Area() << endl << Triangle_3.Perim() << endl << Triangle_3.Area() << endl << endl;
	Collection TrArray = Collection(3);

	TrArray[0] = &Triangle_1;
	TrArray[1] = &Triangle_2;
	TrArray[2] = &Triangle_3;

	cout << TrArray.AllAreas() << endl << TrArray.AllPerim() << endl;

	return 0;
}