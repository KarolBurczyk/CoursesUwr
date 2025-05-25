#ifndef ZAD6_2ARG_H
#define ZAD6_2ARG_H

#include "wyrazenie.h++"

class Dodaj
        :public Wyrazenie
{
protected:
    Wyrazenie *exp;
    Wyrazenie *exp2;
public:
    Dodaj(Wyrazenie *x, Wyrazenie *y);
    double oblicz() override;
    string zapis() override;
};

class Odejmij
        :public Wyrazenie
{
protected:
    Wyrazenie *exp;
    Wyrazenie *exp2;
public:
    Odejmij(Wyrazenie *x, Wyrazenie *y);
    double oblicz() override;
    string zapis() override;
};

class Mnoz
        :public Wyrazenie
{
protected:
    Wyrazenie *exp;
    Wyrazenie *exp2;
public:
    Mnoz(Wyrazenie *x, Wyrazenie *y);
    double oblicz() override;
    string zapis() override;
};

class Dziel
        :public Wyrazenie
{
protected:
    Wyrazenie *exp;
    Wyrazenie *exp2;
public:
    Dziel(Wyrazenie *x, Wyrazenie *y);
    double oblicz() override;
    string zapis() override;
};

class Logarytm
        :public Wyrazenie
{
protected:
    Wyrazenie *exp;
    Wyrazenie *exp2;
public:
    Logarytm(Wyrazenie *x, Wyrazenie *y);
    double oblicz() override;
    string zapis() override;
};

class Modulo
        :public Wyrazenie
{
protected:
    Wyrazenie *exp;
    Wyrazenie *exp2;
public:
    Modulo(Wyrazenie *x, Wyrazenie *y);
    double oblicz() override;
    string zapis() override;
};

class Potega
        :public Wyrazenie
{
protected:
    Wyrazenie *exp;
    Wyrazenie *exp2;
public:
    Potega(Wyrazenie *x, Wyrazenie *y);
    double oblicz() override;
    string zapis() override;
};

#endif
