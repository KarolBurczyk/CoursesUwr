#ifndef ZAD11_STALA_H
#define ZAD11_STALA_H

#include "operand.h++"
#include <iostream>

using namespace std;

class Stala
        :public Opernad
{
protected:
    double val;
public:
    explicit Stala(const string&);
};
#endif
