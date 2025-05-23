#ifndef ZAD11_2ARG_H
#define ZAD11_2ARG_H

#include "operator.h++"
#include <iostream>

using namespace std;

class Bin
        :public Operator
{
public:
    Bin() = default;
    explicit Bin(string);
};

class Add
        :public Bin
{
public:
    Add();
    
};

class Sub
        :public Bin
{
public:
    Sub();
    
};

class Mult
        :public Bin
{
public:
    Mult();
    
};

class Div
        :public Bin
{
public:
    Div();
    
};

class Mod
        :public Bin
{
public:
    Mod();
    
};

class Min
        :public Bin
{
public:
    Min();
    
};

class Max
        :public Bin
{
public:
    Max();
    
};

class Log
        :public Bin
{
public:
    Log();
    
};

class Pow
        :public Bin
{
public:
    Pow();
    
};

#endif
