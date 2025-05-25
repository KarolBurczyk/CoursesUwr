#include "2arg.h++"
#include <cmath>

Dodaj::Dodaj(Wyrazenie *x, Wyrazenie *y)
{
    waga = 1;
    exp = x;
    exp2 = y;
}

double Dodaj::oblicz()
{
    return (exp->oblicz() + exp2->oblicz());
}

string Dodaj::zapis()
{
    return (exp->zapis()+" + "+exp2->zapis());
}

Odejmij::Odejmij(Wyrazenie *x, Wyrazenie *y)
{
    waga = 1;
    exp = x;
    exp2 = y;
}

double Odejmij::oblicz()
{
    return (exp->oblicz() - exp2->oblicz());
}

string Odejmij::zapis()
{
    if(exp2->get_waga() == 1)
    {
        return (exp->zapis() + " - (" + exp2->zapis() + ")");
    }
    else
    {
        return (exp->zapis() + " - " + exp2->zapis());
    }
}

Mnoz::Mnoz(Wyrazenie *x, Wyrazenie *y)
{
    waga = 2;
    exp = x;
    exp2 = y;
}

double Mnoz::oblicz()
{
    return (exp->oblicz() * exp2->oblicz());
}

string Mnoz::zapis()
{
    if(exp->get_waga() == 1)
    {
        if(exp2->get_waga() == 1)
        {
            return ("(" + exp->zapis() + ") * (" + exp2->zapis() + ")");
        }
        else
        {
            return ("(" + exp->zapis() + ") * " + exp2->zapis() );
        }
    }
    if(exp2->get_waga() == 1)
    {
        return (exp->zapis() + " * (" + exp2->zapis() + ")");
    }
    else
    {
        return (exp->zapis() + " * " + exp2->zapis());
    }
}

Dziel::Dziel(Wyrazenie *x, Wyrazenie *y)
{
    waga = 2;
    exp = x;
    exp2 = y;
}

double Dziel::oblicz()
{
    return (exp->oblicz() / exp2->oblicz());
}

string Dziel::zapis()
{
    if(exp->get_waga() == 1)
    {
        if(exp2->get_waga() == 1 or exp2->get_waga() == 2)
        {
            return ("(" + exp->zapis() + ") / (" + exp2->zapis() + ")");
        }
        else
        {
            return ("(" + exp->zapis() + ") / " + exp2->zapis() );
        }
    }
    if(exp2->get_waga() == 1 or exp2->get_waga() == 2)
    {
        return (exp->zapis() + " / (" + exp2->zapis() + ")");
    }
    else
    {
        return (exp->zapis() + " / " + exp2->zapis());
    }
}

Logarytm::Logarytm(Wyrazenie *x, Wyrazenie *y)
{
    waga = 10;
    exp = x;
    exp2 = y;
}

double Logarytm::oblicz()
{
    return (log(exp2->oblicz()) / log(exp->oblicz()));
}

string Logarytm::zapis()
{
    return ("log"+exp->zapis()+"("+exp2->zapis()+")");
}

Modulo::Modulo(Wyrazenie *x, Wyrazenie *y)
{
    waga = 3;
    exp = x;
    exp2 = y;
}

double Modulo::oblicz()
{
    return fmod(exp->oblicz(), exp2->oblicz());
}

string Modulo::zapis()
{
    if(exp->get_waga() < 4)
    {
        if(exp2->get_waga() < 4)
        {
            return ("(" + exp->zapis() + ") % (" + exp2->zapis() + ")");
        }
        else
        {
            return ("(" + exp->zapis() + ") % " + exp2->zapis() );
        }
    }
    if(exp2->get_waga() < 4)
    {
        return (exp->zapis() + " % (" + exp2->zapis() + ")");
    }
    else
    {
        return (exp->zapis() + " % " + exp2->zapis());
    }
}

Potega::Potega(Wyrazenie *x, Wyrazenie *y)
{
    waga = 4;
    exp = x;
    exp2 = y;
}

double Potega::oblicz()
{
    return pow(exp->oblicz(), exp2->oblicz());
}

string Potega::zapis()
{
    if(exp->get_waga() < 10)
    {
        if(exp2->get_waga() < 10)
        {
            return ("(" + exp->zapis() + ") ^ (" + exp2->zapis() + ")");
        }
        else
        {
            return ("(" + exp->zapis() + ") ^ " + exp2->zapis() );
        }
    }
    if(exp2->get_waga() < 10)
    {
        return (exp->zapis() + " ^ (" + exp2->zapis() + ")");
    }
    else
    {
        return (exp->zapis() + " ^ " + exp2->zapis());
    }
}