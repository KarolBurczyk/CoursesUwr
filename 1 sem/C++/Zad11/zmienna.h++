#ifndef ZAD11_ZMIENNA_H
#define ZAD11_ZMIENNA_H

#include "operand.h++"
#include <iostream>
#include <map>
#include <set>

using namespace std;

class Zmienna
        :public Opernad
{
public:
    string nazwa;
    static map<string, double> zmienne;
    static set<string> niedozwolone;
    explicit Zmienna(const string&);
    static void nowaZmienna(const string&, double);
    static void clear();
    string znajdz(string) const;
};
#endif
