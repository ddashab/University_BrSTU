#ifndef LAB3_HEADER_H
#define LAB3_HEADER_H
#include <iostream>

class Geometrical_figure {
protected:
    double V;
    double S;
public:
    double getV() const;
    double getS() const;
    Geometrical_figure& operator = (const Geometrical_figure& right) {
        if (this == &right) {
            return *this;
        }
        V = right.V;
        S = right.S;
        return *this;
    }
    bool operator == (const Geometrical_figure& right) {
        return (V == right.V) && (S == right.S);
    }

    bool operator != (const Geometrical_figure& right) {
        return !((V == right.V) && (S == right.S));

    }
    virtual void Show() = 0;
};

class Cube :public Geometrical_figure {
private:
    double a;
public:
    Cube(double new_a);//constructor with parameters
    void Show() override;
};

class Cylinder :public Geometrical_figure {
private:
    double r, h;
public:
    Cylinder(double new_r, double  new_h);//constructor
    void Show() override;
};
class Tetrahedron :public Geometrical_figure {
private:
    double _a;
public:
    Tetrahedron(double new_a);
    void Show() override;
};
class Arrayptr {
private:
    Geometrical_figure** ptrarr;
    int size = 0;
public:
    void add(Geometrical_figure* figure);
    void print();
    Geometrical_figure* operator [](int index);
};

#endif //LAB3_HEADER_H