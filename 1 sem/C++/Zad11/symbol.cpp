#include "symbol.h++"
#include "iostream"

using namespace std;

Symbol::Symbol(string x)
{
    this->symbol = x;
}

string Symbol::print()
{
    return symbol;
}