#include "stala.h++"
#include <iostream>
#include <cmath>

using namespace std;

double to_stala(const string& name)
{
    if(name == "e")
    {
        return M_E;
    }
    else if(name == "pi")
    {
        return M_PI;
    }
    else if(name == "fi")
    {
        return 1.618033988750;
    }
    else
    {
        clog << "Nie ma takiej stalej";
    }
    return 0;
}

Stala::Stala(const string& name)
    :Opernad(to_string(to_stala(name)))
{
    this->val = to_stala(name);
}

