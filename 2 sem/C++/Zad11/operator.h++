#ifndef ZAD11_OPERATOR_H
#define ZAD11_OPERATOR_H

#include "symbol.h++"

class Operator
        :public Symbol
{
public:
    Operator() = default;
    Operator(string);
};
#endif
