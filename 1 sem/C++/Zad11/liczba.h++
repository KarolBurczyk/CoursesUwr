#ifndef ZAD11_LICZBA_H
#define ZAD11_LICZBA_H
#include "operand.h++"
#include <iostream>

using namespace std;

class Liczba
        :public Opernad
{
protected:
    double val;
public:
    explicit Liczba(const double&);
};
#endif
