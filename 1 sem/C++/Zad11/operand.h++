#ifndef ZAD11_OPERAND_H
#define ZAD11_OPERAND_H

#include "symbol.h++"

class Opernad
        :public Symbol
{
public:
    Opernad() = default;
    explicit Opernad(string);
};
#endif
