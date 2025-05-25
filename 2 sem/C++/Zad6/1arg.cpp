#include "1arg.h++"
#include <cmath>
#include <iostream>
#include <utility>

using namespace std;

Sin::Sin(Wyrazenie *x)
{
    waga = 10;
    exp = x;
}

double Sin::oblicz()
{
    return std::sin(exp->oblicz()/57.3);
}

string Sin::zapis()
{
    return ("sin("+exp->zapis()+")");
}

Cos::Cos(Wyrazenie *x)
{
    waga = 10;
    exp = x;
}

double Cos::oblicz()
{
    return cos(exp->oblicz());
}

string Cos::zapis()
{
    return ("cos("+exp->zapis()+")");
}

Exp::Exp(Wyrazenie *x)
{
    waga = 10;
    exp = x;
}

double Exp::oblicz()
{
    return pow(M_E,exp->oblicz());
}

string Exp::zapis()
{
    return ("(e^"+exp->zapis()+")");
}

Ln::Ln(Wyrazenie *x)
{
    waga = 10;
    exp = x;
}

double Ln::oblicz()
{
    return log(exp->oblicz());
}

string Ln::zapis()
{
    return ("ln("+exp->zapis()+")");
}

Bezwzgl::Bezwzgl(Wyrazenie *x)
{
    waga = 10;
    exp = x;
}

double Bezwzgl::oblicz()
{
    if(exp->oblicz() >= 0)    return exp->oblicz();
    else return (-1)*exp->oblicz();
}

string Bezwzgl::zapis()
{
    return ("|"+exp->zapis()+"|");
}

Przeciw::Przeciw(Wyrazenie *x)
{
    waga = 10;
    exp = x;
}

double Przeciw::oblicz()
{
    return (-1)*exp->oblicz();
}

string Przeciw::zapis()
{
    return ("-"+exp->zapis());
}

Odwrot::Odwrot(Wyrazenie *x)
{
    waga = 10;
    exp = x;
}

double Odwrot::oblicz()
{
    return 1/exp->oblicz();
}

string Odwrot::zapis()
{
    return ("1/"+exp->zapis());
}

