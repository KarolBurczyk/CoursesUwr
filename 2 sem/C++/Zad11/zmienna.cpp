#include "zmienna.h++"
#include <iostream>
#include <cmath>

using namespace std;

map<string, double> Zmienna::zmienne = map<string, double>();

set<string> Zmienna::niedozwolone = {"exit", "set", "clear", "print", "liczba", "e", "pi", "fi", "mod", "min", "max",
"log", "pow", "abs", "sgn", "floor", "ceil", "frac", "sin", "cos", "atan", "acot",
"ln", "exp"};

Zmienna::Zmienna(const string& name)
    :Opernad(znajdz(name))
{
    this->nazwa = name;
}

void Zmienna::nowaZmienna(const string& name, double val)
{
    for (auto & it : Zmienna::zmienne)
        if (it.first == name)
            return to_string(it.second);
    if(name.size() <= 7 and niedozwolone.find(name) == niedozwolone.end())
        zmienne.insert({name, val});
    else
        clog<<"Niedozwolona nazwa zmiennej"<<endl;
}

void Zmienna::clear()
{
    zmienne.clear();
}

string Zmienna::znajdz(string s) const
{
    for (auto & it : Zmienna::zmienne)
        if (it.first == s)
            return to_string(it.second);
    clog<<"Nie ma zdefiniowanej takiej zmiennej"<<endl;
    return "0";
}

