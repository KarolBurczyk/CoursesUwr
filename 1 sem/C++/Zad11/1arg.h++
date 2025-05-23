#ifndef ZAD11_1ARG_H
#define ZAD11_1ARG_H

#include "operator.h++"
#include <iostream>

using namespace std;

class Un
        :public Operator
{
public:
    Un() = default;
    explicit Un(string);
};

class Abs
        :public Un
{
public:
    Abs();
    
};

class Sgn
        :public Un
{
public:
    Sgn();
    
};

class Floor
        :public Un
{
public:
    Floor();
    
};

class Ceil
        :public Un
{
public:
    Ceil();
    
};

class Frac
        :public Un
{
public:
    Frac();
    
};

class Sin
        :public Un
{
public:
    Sin();
    
};

class Cos
        :public Un
{
public:
    Cos();
    
};

class Atan
        :public Un
{
public:
    Atan();
    
};

class Acot
        :public Un
{
public:
    Acot();
    
};

class Ln
        :public Un
{
public:
    Ln();
    
};

class Exp
        :public Un
{
public:
    Exp();
    
};

#endif
