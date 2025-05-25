#ifndef ZAD11_SYMBOL_H
#define ZAD11_SYMBOL_H
#include <iostream>

using namespace std;

class Symbol
{
    string symbol;
public:
    Symbol() = default;
    explicit Symbol(string);
    string print();
};
#endif
