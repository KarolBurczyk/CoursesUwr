#ifndef ZAD6_1ARG_H
#define ZAD6_1ARG_H

#include "wyrazenie.h++"

class Sin
        :public Wyrazenie
{
protected:
    Wyrazenie *exp;
public:
    Sin(Wyrazenie *x);
    double oblicz() override;
    string zapis() override;
};

class Cos
        :public Wyrazenie
{
protected:
    Wyrazenie *exp;
public:
    explicit Cos(Wyrazenie *x);
    double oblicz() override;
    string zapis() override;
};

class Exp
        :public Wyrazenie
{
protected:
    Wyrazenie *exp;
public:
    explicit Exp(Wyrazenie *x);
    double oblicz() override;
    string zapis() override;
};

class Ln
        :public Wyrazenie
{
protected:
    Wyrazenie *exp;
public:
    explicit Ln(Wyrazenie *x);
    double oblicz() override;
    string zapis() override;
};

class Bezwzgl
        :public Wyrazenie
{
protected:
    Wyrazenie *exp;
public:
    explicit Bezwzgl(Wyrazenie *x);
    double oblicz() override;
    string zapis() override;
};

class Przeciw
        :public Wyrazenie
{
protected:
    Wyrazenie *exp;
public:
    explicit Przeciw(Wyrazenie *x);
    double oblicz() override;
    string zapis() override;
};

class Odwrot
        :public Wyrazenie
{
protected:
    Wyrazenie *exp;
public:
    explicit Odwrot(Wyrazenie *x);
    double oblicz() override;
    string zapis() override;
};


#endif
