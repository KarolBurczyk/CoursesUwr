#ifndef ZAD6_EXPRESSION_H
#define ZAD6_EXPRESSION_H
#include <iostream>

using namespace std;

class Wyrazenie
{
protected:
    int waga;
public:
    Wyrazenie& operator=(const Wyrazenie&)=delete;
    Wyrazenie(const Wyrazenie&)=delete;
    Wyrazenie() = default;
    virtual double oblicz();
    virtual string zapis();
    int get_waga();
};


#endif
